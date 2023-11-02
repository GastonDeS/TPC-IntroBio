import argparse
import os
from enum import Enum

class ORF(Enum):
    PROTEIN = 1
    NUCLEOTIDE = 3

def get_orf(method):

    print(f"Saving {method} ORFs from sequence")
    try:
        os.system(f"getorf -sequence {args.input} -outseq {args.output}.orf -find {method.value}")  
    except:
        print("Error: Failed to excute getorf emboss command. Make sure it's installed")
        exit(1)           

def translate():
    print("Translating sequence")
    try:
        os.system(f"transeq -sequence {args.input} -outseq {args.output}.pep")    
    except:
        print("Error: Failed to excute transeq emboss command. Make sure it's installed")
        exit(1)                     

def get_motifs():
    print("Finding motifs")
    try:
        os.system(f"patmatmotifs -sequence {args.input} -outfile {args.output}.patmatmotifs")   
    except:
        print("Error: Failed to excute patmatmotifs emboss command. Make sure it's installed")
        exit(1)         

if __name__ == '__main__':

    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej5.py", description="Execute emboss methods")
    parser.add_argument("--input", help="input sequence file (.fas)", type=str,required=True, metavar="file.fas") 
    parser.add_argument("--output", help="path to save result", type=str, default="sequence", required=False, metavar="filename")
    parser.add_argument("--method", help="emboss method to execute:\n orf_prot finds ORF and saves them as protein sequences\n orf_nt saves them as nucleotide sequences\n translate translates sequence (.pep)\n motifs executes domain analysis (.patmatmotifs) ", type=str, required=True, choices=["orf_prot", "orf_nt", "translate", "motifs", "all"])

    args = parser.parse_args()

    if args.method == "orf_prot" or args.method == "all":
        get_orf(ORF.PROTEIN)
    
    if args.method == "orf_nt" or args.method == "all":
        get_orf(ORF.NUCLEOTIDE)
    
    if args.method == "translate" or args.method == "all": 
        translate()

    if args.method == "motifs" or args.method == "all":
        get_motifs()