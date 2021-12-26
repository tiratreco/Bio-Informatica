import sys

def readArchive(fileName):
	file = open(fileName, 'r')
	k = int(file.readline().split('=')[1])
	dna = file.readline()
	file.close()
	return k, dna

def saveArchive(k, comp):
	file = open('k'+str(k)+'mer.txt', 'w')
	linha = ''
	for f in comp:
		linha += str(f)+', '
	file.write(linha[:-2])
	file.close()

def composition(k, dna):
	comp = []
	for i in range(len(dna)-k+1):
		comp.append(dna[i:i+k])
	return comp

def main(fileName):
	k, dna = readArchive(fileName)
	if (k>len(dna)):
		print('k maior que o DNA')
		return
	comp = composition(k, dna)
	comp.sort()
	saveArchive(k, comp)

main (sys.argv[1])