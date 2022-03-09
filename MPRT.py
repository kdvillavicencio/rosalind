import requests
import pkg.fasta as fs
import pkg.aminoAcid as aa

proteinList = open('rosalind_mprt.txt').read().split('\n')
print(proteinList)

for protein in proteinList:
    proteinFasta = fs.fastaUnpack(requests.get("https://www.uniprot.org/uniprot/" + protein + ".fasta").text)[0][1]
    locs = aa.proteinMotif(proteinFasta)
    if locs != '':
        print(protein)
        print(locs)

