# Trabajo Práctico de Campo

## Overview

This project is designed to perform various bioinformatics tasks using a set of Python scripts. The scripts are organized to carry out specific tasks in a sequential manner, and they are explained below. The project also includes a Docker setup for easy deployment.

## Build Instructions

To build the project, follow these steps:

1. Run the following command to build the Docker image:

   ```
   make docker
   ```

2. If this is the first time you are running the project, use the following command to set up and run the Docker container:

   ```
   make run
   ```

3. Once the initial setup is complete, you can start the container with:

   ```
   make start
   ```

## Example Usage

### Exercise 1

Run the following command to execute the first script:

```bash
python3 ./ex1.py --input Genbank/rb1.gbk --output "orfs"
```

### Exercise 2

Execute the second script with either protein or nucleotide blast method:

```bash
python3 ./ex2.py --input orfs/NM_000231.3 --output blast_results --method ncbi-blast-2.15.0+/bin/blastp
```

OR

```bash
python3 ./ex2.py --input orfs/NM_000231.3 --output blast_results --method ncbi-blast-2.15.0+/bin/blastn
```

### Exercise 3

Run the third script with the following command:

```bash
python3 ./ex3.py --input blast_results/orf0_876.xml --fasta-msa ex3AuxFile.fasta
```

To get the final output in a file, we use the following link:

`https://www.ebi.ac.uk/Tools/msa/clustalo/`

And then we copy the ex3AuxFile.fasta into the placeholder of the webpage and download the output file. (msa/alignedmultipleGapsMuscle)

### Exercise 4

Execute the fourth script using the output from Example 1:

```bash
python3 ./ex4.py --input orfs/NM_000231.3/orf0_876.fas --method orf_prot --output test_prote
```

### Exercise 5

Run the fifth script by providing the path to a JSON file and sequence parameters:

```bash
python3 ./ex5.py --json-path /path/to/json --sequence "example_sequence"
```

Make sure to replace `/path/to/json` with the actual path to your JSON file and `"example_sequence"` with the desired sequence.

Feel free to customize and adapt these commands based on your specific use case and file paths.

## Contributors

- Chao, Florencia
- De Luca, Juan Manuel
- De Schant, Gaston
- Flores Levalle, Magdalena
