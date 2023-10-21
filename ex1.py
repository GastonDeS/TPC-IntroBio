from Bio import SeqIO
import os
import argparse

CODON_LEN = 3
STOP_CODONS = ["TAA", "TAG", "TGA"]
START_CODON = "ATG"


def find_stop_codon(sequence, start):
    for i in range(start, len(sequence), CODON_LEN):
        codon = sequence[i:i + CODON_LEN]
        if codon in STOP_CODONS:
            return i
    return -1


def search_start_codon(sequence):
    start = 0
    start = sequence.find(START_CODON, start)
    if start == -1:
        return ""
    end = find_stop_codon(sequence, start) + CODON_LEN
    if end != -1:
        return sequence[start:end]


def create_output_directory(output_path):
    os.makedirs(output_path, exist_ok=True)


def save_orf_to_file(orf, directory, index):
    with open(f"{directory}/orf{index}_{len(orf)}.fas", "w") as f:
        f.write(f">{index} Length {len(orf)}\n")
        f.write(orf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="ex1.py", description="Reads one nucleotide sequences in genbank format (.gbk) and saves it in fasta format (.fas)")
    parser.add_argument("--input", help="path to GENBANK input file (.gbk)", type=str, metavar="file.gbk", required=True)
    parser.add_argument("--output", help="path to save FASTA output file", type=str, metavar="path/to/file", default="ORF", required=False)
    args = parser.parse_args()

    try:
        records = SeqIO.parse(args.input, "genbank")
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        exit(1)

    for record in records:
        sequence = str(record.seq)
        orfs = []

        for i in range(CODON_LEN):
            orfs.append(search_start_codon(sequence[i:]))
            sequence = sequence[::-1]

        for i in range(CODON_LEN):
            orfs.append(search_start_codon(sequence[i:]))

        if len(orfs) == 0:
            print("No ORFs found")
            exit()

        output_directory = f"{args.output}/{record.id}/"
        create_output_directory(output_directory)

        for i, orf in enumerate(orfs):
            save_orf_to_file(orf, output_directory, i)