# ENA bulk download
A lightweight command-line tool that automates the bulk download of nucleotide sequences from the European Nucleotide Archive (ENA) using accession IDs provided in a tab-delimited table. It retrieves sequences in FASTA format and compiles them into a single output file.

This is especially useful when you **first generate a table of results using the [ENA Query Builder](https://www.ebi.ac.uk/ena/browser/text-search?query=)**, export the table, and then pass it to this tool to **download all sequences via the ENA API.**

The ENA web interface and query builder allow you to find and export metadata for large numbers of sequences, but **downloading the actual sequence data in bulk** is not optimal directly through the UI, especially for a massive query.

**ENA bulk download** fills that gap by:
- Accepting an exported **TSV table** from the ENA Query Builder
- Reading the `accession` column
- Downloading each sequence via the ENA API
- Saving all retrieved sequences into **one combined FASTA file**

## Requirements

- Python 3.6+
- [requests](https://pypi.org/project/requests/) module

Install dependencies:

```bash
pip install requests
```

## Example usage

```
python ena_bulk_download.py my_query_table.tsv my_output_seqs.fasta
```


## Example tsv input 

This **requires** the accession column but other fields may vary based on your built query. 

```
accession	base_count	description	tax_id	host
AY505112	39853	Vibriophage VP2, complete genome.	260372	
CP124949	28901	Enterococcus phage1_EF62phi, complete genome.	3045168	Enterococcus faecalis EfsC43
EU876853	47453	Iodobacteriophage phiPLPE, complete genome.	551895	Iodobacter sp. CdM7
MN016939	31834	Bacteriophage R18C, complete genome.	2592161	
AF323668	35538	Bacteriophage bIL285, complete genome.	151535	Lactococcus lactis IL1403
MG022440	138073	Phage 206, complete genome.	2048063	
MN994500	50922	Phage NBSal001, complete genome.	2704941	
ON970599	45847	Gordoniaphage Biskit, complete genome.	2965189	
AF323673	15179	Bacteriophage bIL312, complete genome.	151539	Lactococcus lactis IL1403
AY082070	33507	Bacteriophage phi3626, complete genome.	190478	Clostridium perfringens
DQ029335	39503	Vibriophage VP4, complete genome.	329886	
KF626668	55601	Phage Salvo, complete genome.	1415147	Xylella fastidiosa
MN994501	120250	Phage NBSal002, complete genome.	2712976	
MT774389	101082	CrAssphage cr116_1, complete genome.	2772073
```

## Example output

```
>ENA|AY505112|AY505112.1 Vibriophage VP2, complete genome.
ATGTATTTTAATTATAGCATGCAATAGGGCGGTTGTCAATAGTCTTGTGTGTTAAA...
>ENA|CP124949|CP124949.1 Enterococcus phage1_EF62phi, complete genome.
TTTGTTTCCTTTAATGTCTCTTGTGTGTAATTTATTGCTGTCTGTGCGATCGAT...
>ENA|EU876853|EU876853.1 Iodobacteriophage phiPLPE, complete genome.
ATGTTAGTTAAAGAAGTGGCAGAAACTTTGGGCGTGTCTGAGCAGTGGGTACGCAAGC...
```

## Acknowedgements 

- [ENA Portal API](https://www.ebi.ac.uk/ena/portal/api/swagger-ui/index.html)
