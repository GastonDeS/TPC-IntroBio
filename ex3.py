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

    if hit_elements:
        # add our nucleotido
        ourHit = hit_elements[0].find("Hit_hsps/Hsp/Hsp_qseq").text
        
        for hit_element in hit_elements[:10]:
            hit_id = hit_element.find("Hit_accession").text
            hit_ids.append(hit_id)
        return ourHit, hit_ids
    else:
        print("No Hit elements found in the XML.")
        
    return hit_ids

def fetch_fasta_from_genbank(accession):
    Entrez.email = None  # Set to None if you prefer not to provide an email address
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ex3.py", description="Execute Multiple Sequence Alignment with Clustalw")
    parser.add_argument("--input", help="Input file (orf.xml)", type=str, required=True)
    parser.add_argument("--fasta-msa", help="fasta prepared for msa", type=str, required=True)
    args = parser.parse_args()

    outHit, accessions = parseOrf(args.input)
    top10fastas = ''
    for accession in accessions:
        fasta = fetch_fasta_from_genbank(accession)
        top10fastas += ">%s\n%s\n" % (fasta.id, fasta.seq)

    top10fastas += ">%s\n%s\n" % (1, outHit)


    with open(args.fasta_msa, "w") as file:
      file.write(top10fastas)