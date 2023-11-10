import subprocess
import argparse
from shutil import which
from enum import Enum
# from Bio import SeqIO, AlignIO, Seq, SeqRecord
# from Bio.Align.Applications import ClustalwCommandline
# from Bio.Application import ApplicationError
import argparse
import xml.etree.ElementTree as ET

def parseOrf(orfFile):
    
    # Load the XML file
    tree = ET.parse(orfFile)
    root = tree.getroot()

    # Find all Hit elements
    hit_elements = root.findall(".//Hit")

    hit_ids = []

    # Check if any Hit elements are found
    if hit_elements:
        # Iterate over each Hit element
        for hit_element in hit_elements[:10]:
            # Access information within each Hit element
            hit_id = hit_element.find("Hit_accession").text
            hit_ids.append(hit_id)
    else:
        print("No Hit elements found in the XML.")
        
    return hit_ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ex3.py", description="Execute Multiple Sequence Alignment with Clustalw")
    parser.add_argument("--input", help="Input file (orf.xml)", type=str, required=True)
    parser.add_argument("--output", help="Output file", type=str, required=False)
    parser.add_argument("--fastaPath", help="Path to fasta file", type=str, required=True)
    args = parser.parse_args()

    tree = ET.parse(args.fastaPath)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)

    in_file = args.input
    out_file = args.output

    extension = in_file.split(".")[-1]
    
    ids = parseOrf(in_file)
    
    print(ids)

    # perform_msa(in_file, out_file)