with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()

genes = {}
for line in lines:
    line = line.strip()
    if line.startswith('>'):
        name = line[1:].split()[0]
    else:
        genes[name] = line

for name, seq in genes.items():
    print(name, len(seq))
