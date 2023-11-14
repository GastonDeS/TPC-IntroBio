import os
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import argparse
import threading

#me tira error de ssl connection. Check. 
def online_blastn(file, args):
    try:
        filepath = os.path.join(args.input, file) if os.path.isdir(args.input) else args.input
        seq = SeqIO.read(filepath, format="fasta")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    try:
        result = NCBIWWW.qblast("blastn", "nt", seq.seq)
    except Exception as e:
        print(f"Error: NCBI Remote blastn failed: {e}")
        exit(1)
    file = file.split(".")[0]
    with open(os.path.join(args.output, f"{file}.xml"), "w") as f:
        print(f"Saving results in {args.output}/{file}.xml")
        f.write(result.read())


def local_blastp(file, args):
    try:
        filepath = os.path.join(args.input, file) if os.path.isdir(args.input) else args.input
        record = SeqIO.read(filepath, format="fasta")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    seqprot = record.seq.translate(stop_symbol="")
    name = file.split(".")[0]
    path = os.path.join(args.output, f"{name}_protein.fasta")
    os.makedirs(args.output, exist_ok=True)
    with open(path, "w") as f:
        print(f"Saving results in {path}")
        f.write(f">{record.id}\n")
        f.write(seqprot.__str__())
    command = f'blastp -query {path} -db /root/swissprot -outfmt 5 -out {args.output}/{file}.xml"'
    try:
        os.system(command)
    except Exception as e:
        print(f"Error: Local BLASTP failed: {e}")
        exit(1)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def run_blast(target, args):
    threads = []
    input_path = args.input
    if is_file(input_path):
        print("Running BLAST for a single file")
        target(input_path, args)
        return
    if not is_dir(input_path):
        print(f"Error: {input_path} is not a file or directory")
        exit(1)
    files = os.listdir(input_path)
    for file in files:
        print(f"BLAST for file {file}")
        t = threading.Thread(target=target, args=(file, args))
        t.start()
        threads.append(t)
    for i, t in enumerate(threads):
        try:
            t.join()
        except Exception as e:
            print(f"Error: BLAST failed for file {files[i]}: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="ex2.py", description="Executes BLAST query using NCBI database")
    parser.add_argument("--input", help="path to the sequence to BLAST", type=str, metavar="path/to/file", required=True)
    parser.add_argument("--output", help="path to folder to save BLAST output in .xml format. Defaults to creating a /blast_output folder", type=str, metavar="path/to/file", default="blast_output", required=False)
    parser.add_argument("--method", help="blastn or blastp. Defaults to blastn, blastp requires a local swissprot database", type=str, metavar="blastn|blastp", default="blastn", required=False, choices=["ncbi-blast-2.13.0+/bin/blastn", "ncbi-blast-2.13.0+/bin/blastp"])
    args = parser.parse_args()
    if args.method == "ncbi-blast-2.13.0+/bin/blastn":
        target = online_blastn
    elif args.method == "ncbi-blast-2.13.0+/bin/blastp":
        target = local_blastp
    else:
        print("Please enter a blastp or blastn method")
        exit(1)
    print(f"Starting {args.method} with {args.input}")
    run_blast(target, args)