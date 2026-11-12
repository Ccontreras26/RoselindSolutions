with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()

count = 0
for line in lines:
    if line.startswith('>'):
        count += 1

print("Number of sequences:", count)
print("Total lines in file:", len(lines))
