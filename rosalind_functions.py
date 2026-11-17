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
def GC(sequences):
    best = ""
    b_gc = 0

    for seq_id in sequences:
        dna = sequences[seq_id]
        score = gc_percent(dna)

        if score > best_gc:
            b_gc = score
            best = seq_id

    return best, b_gc
    
HAMM

PROT

SUBS

PRTM

REVP

TRAN
