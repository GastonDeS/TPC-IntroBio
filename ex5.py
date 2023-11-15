import json
import argparse
from Bio.SeqUtils import MeltingTemp
from Bio.Seq import Seq

def load_config(config_file):
    with open(config_file, "r") as f:
        return json.load(f)

def design_primers(sequence, config):
    primer_length_range = config["primer_length_range"]
    gc_content_range = config["gc_content_range"]
    max_gc_terminal = config["max_gc_terminal"]
    max_melting_temperature = config["max_melting_temperature"]

    primers = []

    for i in range(len(sequence)):
        for j in range(i + primer_length_range[0], min(i + primer_length_range[1], len(sequence))):
            primer = sequence[i:j]
            gc_content = (primer.count("G") + primer.count("C")) / len(primer)
            gc_terminal = (primer[:2].count("G") + primer[-2:].count("G")) / 4.0
            melting_temp = MeltingTemp.Tm_Wallace(primer)
            
            if (
                gc_content * 100 >= gc_content_range[0]
                and gc_content * 100 <= gc_content_range[1]
                and gc_terminal <= max_gc_terminal
                and melting_temp <= max_melting_temperature
            ):
                primers.append(primer)

    return primers

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="ex5.py", description="Primers generator")
    parser.add_argument("--json", help="path to json configuration file (.json)", type=str,required=True, metavar="file.json") 
    parser.add_argument("--sequence", help="sequence from which we want to create primers", type=str, required=True, metavar="sequence")

    args = parser.parse_args()

    config = load_config(args.json)
    # Replace the following line with your transcript sequence
    sequence = Seq(args.sequence)

    # Design primers
    primers = design_primers(sequence, config)

    # Print or use the designed primers
    f = open("primers.txt", "w")
    for primer in primers:
        f.write(str(primer) + "\n")
    f.close()