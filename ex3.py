import subprocess
import argparse
from shutil import which
from enum import Enum
from Bio import SeqIO, AlignIO, Seq, SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Application import ApplicationError
import argparse

def perform_msa(in_file, out_file):
    try:
        if which("clustalw2") is None:
            print(f"Error: Clustalw2 is not installed. Please make sure it is installed.")
            exit(1)

        clustalw_cline = ClustalwCommandline("clustalw2", infile=in_file, outfile=out_file)
        clustalw_cline()

    except (subprocess.CalledProcessError, OSError) as e:
        print(f"Error: Unable to perform MSA with Clustalw2: {e}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ex3.py", description="Execute Multiple Sequence Alignment with Clustalw")
    parser.add_argument("--input", help="Input file (.fas)", type=str, required=True)
    parser.add_argument("--output", help="Output file", type=str, required=True)
    args = parser.parse_args()

    in_file = args.input
    out_file = args.output

    extension = in_file.split(".")[-1]

    perform_msa(in_file, out_file)