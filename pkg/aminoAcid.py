import pandas as pd

map = open('.\pkg\proteinmap.txt').read()
map = map.split(sep='\n')
proteinmap = {}
proteinlist = pd.DataFrame(columns=['codon', 'amino_acid'])

for key in map:
    key = key.strip().split(' ')
    proteinmap[key[0]] = key[1]
    proteinlist = proteinlist.append(pd.DataFrame([[key[0], key[1]]], columns=['codon', 'amino_acid']))

codonCount = proteinlist['amino_acid'].value_counts()

# Codon to Amino Acid
def codonTranslate(codon):
    return proteinmap[codon]

# String to Amino Acid chain
def stringTranslate(string):
    protein = ''
    for x in range(int(len(string)/3)):
        codon = string[3*x:(3*x)+3]
        protein += codonTranslate(codon)
    return protein

# Possible Codons given aminoAcid
def codonProbability(amino_acid):
    return float(codonCount[amino_acid])
