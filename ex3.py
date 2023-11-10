import subprocess
import argparse
from shutil import which
from enum import Enum
from Bio.Align.Applications import ClustalwCommandline
import argparse
import xml.etree.ElementTree as ET
from Bio import Entrez, SeqIO


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

def fetch_fasta_from_genbank(accession):
    Entrez.email = None  # Set to None if you prefer not to provide an email address
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record

def perform_msa(inputs, output):
  # Set up the CrustalW command
  crustal_cmd = ClustalwCommandline("crustalw2", infile=inputs, outfile=output)

  print(crustal_cmd)
  crustal_cmd()
  return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ex3.py", description="Execute Multiple Sequence Alignment with Clustalw")
    parser.add_argument("--input", help="Input file (orf.xml)", type=str, required=True)
    parser.add_argument("--output", help="Output file", type=str, required=False)
    args = parser.parse_args()

    accessions = parseOrf(args.input)
    top10fastas = ''
    for accession in accessions:
        fasta = fetch_fasta_from_genbank(accession)
        top10fastas += ">%s\n%s\n" % (fasta.id, fasta.seq)

    

    with open(args.output, "w") as file:
      file.write(top10fastas)

    print(top10fastas)

    perform_msa(top10fastas, args.output)