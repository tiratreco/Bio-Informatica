start = ["AUG"]
stop = ["UAA","UAG","UGA"]

geneticCode = {
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
    'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L', 
    'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', 
    'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

#Gustavo André

rna_m = open('rna_m.txt', 'r').read()
proteinas_arq = open('proteinas.txt', 'w')

iniciou = False
for i in range(0, len(rna_m), 3):
    codon = rna_m[i:i+3]
    if codon in start:
        iniciou = True
        continue
    if iniciou:
        if codon in stop:
            break;
        proteinas_arq.write(geneticCode[codon])

proteinas_arq.close()