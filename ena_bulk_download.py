import requests
import csv
import sys
import os

# === ENA FASTA API URL ===
ENA_FASTA_URL = "https://www.ebi.ac.uk/ena/browser/api/fasta/{}"

# === READ ACCESSION IDs FROM TSV FILE ===
def read_accessions(file_path):
    accession_list = []
    with open(file_path, newline='') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in reader:
            accession = row.get("accession")
            if accession:
                accession_list.append(accession.strip())
    return accession_list

# === DOWNLOAD FASTA FROM ENA ===
def download_fasta(accession):
    url = ENA_FASTA_URL.format(accession)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# === MAIN FUNCTION ===
def download_all_fastas(input_table, output_fasta):
    accessions = read_accessions(input_table)
    success_count = 0
    fail_list = []

    with open(output_fasta, 'w') as outfile:
        for acc in accessions:
            print(f"Downloading {acc}...")
            fasta = download_fasta(acc)
            if fasta:
                outfile.write(fasta)
                if not fasta.endswith('\n'):
                    outfile.write('\n')
                success_count += 1
            else:
                print(f"? Failed to download: {acc}")
                fail_list.append(acc)

    total = len(accessions)
    print("\n=== Download Summary ===")
    print(f"Success: {success_count}/{total}")
    print(f"Failed : {len(fail_list)}")
    if fail_list:
        print("Failed accessions:")
        for f in fail_list:
            print(f"  - {f}")
    print(f"\nCombined FASTA saved to: {output_fasta}")

# === ENTRY POINT ===
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {os.path.basename(__file__)} <input_table.tsv> <output.fasta>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    download_all_fastas(input_file, output_file)
