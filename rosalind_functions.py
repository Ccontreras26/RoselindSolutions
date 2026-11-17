#DNA
def DNA(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")
#RNA
def RNA(s):
    return s.replace("T", "U")
#REVC
def REVC(s):
    bps = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([bps[base] for base in s[::-1]])
#GC
def gc(seq):
    count_C = seq.count("C")
    count_G = seq.count("G")
    gc_% = ((count_C + count_G) / len(seq)) * 100
    return gc_%
    
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
        codons = s[i: i + 3]
        protein.append(codon_table.get(codons, ''))
           return "".join(protein)
    
#SUBS
def SUBS(s, t):
    positions = []
    
    for i in range(len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
            positions.append(i + 1)
            
    return positions
    
#PRTM
def PRTM(P):
    mass_table = {
        "A": 71.03711,
        "C": 103.00919,
        "D": 115.02694,
        "E": 129.04259,
        "F": 147.06841,
        "G": 57.02146,
        "H": 137.05891,
        "I": 113.08406,
        "K": 128.09496,
        "L": 113.08406,
        "M": 131.04049,
        "N": 114.04293,
        "P": 97.05276,
        "Q": 128.05858,
        "R": 156.10111,
        "S": 87.03203,
        "T": 101.04768,
        "V": 99.06841,
        "W": 186.07931,
        "Y": 163.06333
    }

    total_weight = 0.0

    for amino_acid in P:
        total_weight += mass_table[amino_acid]

    return round(total_weight, 3)
    

#REVP
def REVP(s):
    bps= {"A": "T", "T": "A", "C": "G", "G": "C"}
    results = []

    for i in range(len(s)):
        for length in range(4, 13, 2):
            if i + length <= len(s):
                piece = s[i : i + length]
                
                rev_comp = ""
                for base in piece[::-1]:
                    rev_comp += bps[base]

                if piece == rev_comp:
                    results.append((i + 1, length))

    return results
    
#TRAN
def TRAN(DNAstring1: str, DNAstring2: str) -> float:
    transitions_set = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
    transitions = 0
    transV = 0

    for b1, b2 in zip(DNAstring1, DNAstring2):
        if b1 != b2:
            if (b1, b2) in transitions_set:
                transitions += 1
            else:
                transV += 1

    return transitions / transV
    
