import pkg.fasta as fasta 
import pandas as pd

s = open('rosalind_cons.txt').read()
sList = fasta.fastaUnpack(s)

profile = pd.DataFrame(0, columns=range(len(sList[0][1])),index=['A', 'C', 'G', 'T'])
def appendProfile(base, pos):
    profile.at[base,pos] += 1

for i,j in sList:
    for k in range(len(j)):
        appendProfile(j[k],k)

consensus = ''
A, C, G, T = 'A:', 'C:', 'G:', 'T:'
for i in range(len(profile.columns)):
    consensus += profile[i].idxmax()
    A += ' ' + str(profile.iloc[0][i])
    C += ' ' + str(profile.iloc[1][i])
    G += ' ' + str(profile.iloc[2][i])
    T += ' ' + str(profile.iloc[3][i])

with open('output.txt', 'w') as f:
    f.write(consensus + '\n' + A + '\n' + C + '\n' + G + '\n' + T)