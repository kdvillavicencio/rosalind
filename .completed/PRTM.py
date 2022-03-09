import pkg.aminoAcid as aa

s = open('rosalind_prtm.txt').read()
print(round(aa.proteinMass(s),3))

