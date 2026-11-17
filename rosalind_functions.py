#DNA
def DNA(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")
#RNA
def RNA(s):
    return s.replace("T", "U")
#REVC
def REVC(s):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complements[base] for base in s[::-1]])
#GC
def gc_percent(dna):
    return ((dna.count("G") + dna.count("C")) / len(dna)) * 100

def GC(fasta_text):
    best_id = ""
    best_gc = 0.0
    current_id = ""
    current_dna = ""

    for line in fasta_text.splitlines():
        if line.startswith(">"):
            if current_dna != "":
                score = gc_percent(current_dna)
                if score > best_gc:
                    best_gc = score
                    best_id = current_id
            current_id = line[1:]
            current_dna = ""
        else:
            current_dna += line

    if current_dna != "":
        score = gc_percent(current_dna)
        if score > best_gc:
            best_gc = score
            best_id = current_id

    return best_id, best_gc
    
    
#HAMM
def HAMM(s, t):
    mutations = 0
    
    for i in range(len(s)):
        if s[i] != t[i]:
            mutations += 1
            
    return mutations

#PROT
def PROT(s):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    protein = ""

    for i in range(0, len(s), 3):
        codons = s[i:i+3]
        amino_acid = codon_table[codons]

        if amino_acid == "Stop":
            break

        protein += amino_acid

    return protein
    
#SUBS
def SUBS(s, t):
    locations = []
    
    for i in range(len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
            locations.append(i + 1)
            
    return locations
    
PRTM

REVP

TRAN
