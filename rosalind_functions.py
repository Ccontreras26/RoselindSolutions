#DNA 
DNA
def DNA(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")
RNA
def RNA(s):
    return s.replace("T", "U")
REVC
def REVC(s):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complements[base] for base in s[::-1]])
GC
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
    
    
HAMM

PROT

SUBS

PRTM

REVP

TRAN
