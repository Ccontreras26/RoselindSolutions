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

HAMM

PROT

SUBS

PRTM

REVP

TRAN
