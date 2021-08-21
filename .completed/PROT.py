import pkg.translate as md

s = open('rosalind_prot.txt').read()
protein = ''

for x in range(int(len(s)/3)):
    codon = s[3*x:(3*x)+3]
    protein += md.codonTranslate(codon)

protein = protein.replace('Stop','')
print(protein)