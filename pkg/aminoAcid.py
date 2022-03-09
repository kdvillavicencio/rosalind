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

mass = open('.\pkg\proteinmass.txt').read()
mass = mass.split(sep='\n')
proteinmass = {}

for key in mass:
    key = key.strip().split('   ')
    proteinmass[key[0]] = key[1]

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

# Calculate Protein Mass
def proteinMass(string):
    proteinMass = 0
    for i in string:
        proteinMass += float(proteinmass[i])
    return proteinMass

#def parseMotif(motif):
# make a dict for [motif_qualifier] and [motif_letters] that can be looped and compared with an amino acid

def proteinMotif(protein):
    locations = ''
    motif_length = 4
    for i in range(len(protein) - motif_length):
        temp = protein[i:i+motif_length]
        #print(temp)
        c1 = temp[0] == 'N'
        c2 = temp[1] != 'P'
        c3 = temp[2] == 'S' or temp[2] == 'T'
        c4 = temp[3] != 'P'
        if c1*c2*c3*c4 == True:
            locations += str(i+1) + ' '
    return locations



