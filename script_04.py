with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()

out = open('gc_report.txt', 'w')

for gc = (line.count('G') + line.count('C')) / len(line) * 100
        out.write(name + '\t' + str(round(gc, 1)) + '\n')
