#Gustavo André
match = 1
mismatch = -1
gap = -2

dna = open('dna.txt', 'r')
vertical = dna.readline()[:-1]
horizontal = dna.readline()
#vertical, horizontal = 'UCGUUACGUAUCGUGUUUACGUUACGCAACACGACCUUACCCUACCGCAGGGCAGCACAAAACGCAUGCUUUCCCCACAAUGUGCAUCCGCGCAAGUUGCCCAUCACGCCAUUUCAGGGGGACGUAACCCGAAAUUGUGUCCGAACGAAAUUGCAAGUCAAGGGGCUUGGAAGCUAAUGAUAAUGCCCCGAUAUCAACCA', 'UCGUAUCGUGUUUACGCAACACGACCGCAGGGCAGCACAAAACGCAUGCUUUCCCCACAAUGUGCAUCCGCGCAAUUCAAGUUGCCCAUCCCAUCACGCCAUUUCAGGGGGACGUAACCCGAAAGUAAAUUGU'

def printMat(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('  '+str(matrix[i][j]['score']), end='')
        print('')

def iniciarMatriz():
    matrix = []
    for i in range(len(vertical)+1):
        linha = [None]*(len(horizontal)+1)
        matrix.append(linha)
    for i in range(len(vertical), -1, -1):
        matrix[i][0] = {'score': (len(vertical)-i)*gap}
    for i in range(len(horizontal)+1):
        matrix[len(vertical)][i] = {'score': i*gap}
    return matrix

def preencherMatriz(matrix):
    for l in range(len(vertical)-1, -1, -1):
        for c in range(1, len(horizontal)+1):
            val = {}
            matrix[l][c] = {}
            val['dia'] = matrix[l+1][c-1]['score']
            val['dia'] = val['dia'] + (match if (vertical[len(vertical)-1-l] == horizontal[c-1]) else mismatch)
            val['hor'] = matrix[l][c-1]['score'] + gap
            val['ver'] = matrix[l+1][c]['score'] + gap
            matrix[l][c]['dir'] = max(val, key=val.get)
            matrix[l][c]['score'] = val[matrix[l][c]['dir']]

def backTracing(matrix): 
    l = 0
    c = len(horizontal)
    fita1 = []
    fita2 = []
    score = matrix[l][c]['score']
    while (l != len(vertical) and c != 0):
        if matrix[l][c]['dir'] == 'ver':
            fita1.append(vertical[len(vertical)-1-l])
            fita2.append('_')
            l += 1
        elif matrix[l][c]['dir'] == 'hor':
            fita1.append('_')
            fita2.append(horizontal[c-1])
            c -= 1
        else:
            fita1.append(vertical[len(vertical)-1-l])
            fita2.append(horizontal[c-1])
            l += 1
            c -= 1
    arq = open('alinhamento.txt', 'w')
    arq.write('score: '+str(score)+'\n')
    fita1.reverse()
    fita2.reverse()
    for e in fita1: arq.write(str(e))
    arq.write('\n')
    for e in fita2: arq.write(str(e))

matrix = iniciarMatriz()
preencherMatriz(matrix)
backTracing(matrix)
printMat(matrix)