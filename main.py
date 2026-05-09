
# FASTA Sequence Analyzer - Clean Version

def read_fasta(sequence):
    return sequence.replace("\n", "").replace(" ", "").upper()

def gc_content(seq):
    if len(seq) == 0:
        return 0
    return ((seq.count("G") + seq.count("C")) / len(seq)) * 100

def find_orf(seq):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq)-2, 3):
                if seq[j:j+3] in stop_codons:
                    orfs.append(seq[i:j+3])
                    break

    return orfs

def main():
    print("=== FASTA SEQUENCE ANALYZER ===")

    seq = input("Enter DNA Sequence: ")
    sequence = read_fasta(seq)

    print("\n--- Analysis Results ---")
    print("Length:", len(sequence))
    print("GC Content:", round(gc_content(sequence), 2), "%")
    print("ORFs Found:", find_orf(sequence))

if __name__ == "__main__":
    main()
