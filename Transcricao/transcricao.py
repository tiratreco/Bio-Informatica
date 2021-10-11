#Gustavo André

dna = open('dna.txt', 'r').read()
rna_arq = open('rna_m.txt', 'w')

trad = {
	'A':'U',
	'T':'A',
	'G':'C',
	'C':'G' 
}

for e in dna:
	rna_arq.write(trad[e])

rna_arq.close()
