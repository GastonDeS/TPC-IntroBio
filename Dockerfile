FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3-pip wget
RUN pip3 install biopython
WORKDIR /root

RUN wget "http://www.clustal.org/download/current/clustalw-2.1-linux-x86_64-libcppstatic.tar.gz"

#extract clustalw2
RUN tar -xvzf "clustalw-2.1-linux-x86_64-libcppstatic.tar.gz"
RUN mv clustalw-2.1-linux-x86_64-libcppstatic/clustalw2 /usr/local/bin/clustalw2
RUN chmod +x /usr/local/bin/clustalw2

RUN wget "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/ncbi-blast-2.13.0+-x64-linux.tar.gz"
RUN tar -xvzf "ncbi-blast-2.13.0+-x64-linux.tar.gz"
RUN wget "https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz"
RUN gunzip "swissprot.gz"
RUN mv ncbi-blast-2.13.0+/bin/* /usr/local/bin/
RUN "makeblastdb" -in swissprot -dbtype prot

RUN apt-get install -y emboss
RUN wget "ftp://ftp.expasy.org/databases/prosite/prosite.dat"
RUN wget "ftp://ftp.expasy.org/databases/prosite/prosite.doc"
RUN mkdir db
RUN mv prosite.dat db/
RUN mv prosite.doc db/

RUN prosextract -prositedir db