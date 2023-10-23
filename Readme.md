Build:
make docker
make run (solo si es la primera vez que lo corres)
make start

Ex 1 
python3 ./ex1.py --input Genbank/rb1.gbk --output "orfs"

Ex 2

python3 ./ex2.py --input orfs/NM_000321.3 --output blast_results --method ncbi-blast-2.13.0+/bin/blastp

Ex3 

python3 ./ex3.py --input msa/msa.fasta --output msa/alignedmultipleGapsMuscle