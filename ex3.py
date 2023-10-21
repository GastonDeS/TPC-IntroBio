import subprocess
import argparse
from shutil import which
from enum import Enum
from Bio import SeqIO, AlignIO, Seq, SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Application import ApplicationError
from Bio.Align.Applications import MuscleCommandline
import argparse
from shutil import which



class MSA(Enum):
    CLUSTALW = 1
    MUSCLE = 2

def is_method_installed(method):
    if method == MSA.CLUSTALW:
        return which("clustalw2") is not None
    elif method == MSA.MUSCLE:
        return which("muscle") is not None
    else:
        return False

def perform_msa(in_file, out_file, method):
    try:
        if not is_method_installed(method):
            print(f"Error: {method.name} is not installed. Please make sure it is installed.")
            exit(1)

        if method == MSA.CLUSTALW:
            clustalw_cline = ClustalwCommandline("clustalw2", infile=in_file, outfile=out_file)
            clustalw_cline()

        elif method == MSA.MUSCLE:
            command = ["muscle", "-in", in_file, "-out", out_file]
            subprocess.run(command, check=True)

    except (subprocess.CalledProcessError, OSError) as e:
        print(f"Error: Unable to perform MSA with {method.name}: {e}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ej3.py", description="Execute Multiple Sequence Alignment with Muscle")
    parser.add_argument("--input", help="Input file (.fas)", type=str, required=True)
    parser.add_argument("--output", help="Output file", type=str, required=True)
    args = parser.parse_args()

    in_file = args.input
    out_file = args.output

    extension = in_file.split(".")[-1]
    if extension not in ["fas", "fasta"]:
        print("Error: Please enter a .fas or .fasta file")
        exit(1)

    perform_msa(in_file, out_file, MSA.MUSCLE)