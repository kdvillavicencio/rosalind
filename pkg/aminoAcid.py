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

# Possible Codons given aminoAcid
def codonProbabilty(amino_acid):
    return float(codonCount[amino_acid])
