Build:
make docker
make run (solo si es la primera vez que lo corres)
make start (corres esto solo directamente si ya lo tenes compilado/build)

Ex 1
python3 ./ex1.py --input Genbank/rb1.gbk --output "orfs"

Ex 2

python3 ./ex2.py --input orfs/NM_000321.3 --output blast_results --method ncbi-blast-2.13.0+/bin/blastn
(blastp no funciona)

Ex3

python3 ./ex3.py --input blast_results/orf0_2787 --fasta-msa=ex3AuxFile.fasta --output msa/alignedmultipleGapsMuscle

Ex4

python3 ./ex4.py --input orfs/NM_000321.3/orf0_2787.fas --method orf_prot --output test_prote (el input es el archivo de salida del ex 1)

Ex5
python3 ./ex5.py (hay q hacer q reciba el path al json y la secuencia por params)
