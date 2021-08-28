import pkg.fasta as fs 
import pkg.aminoAcid as aa

s = fs.fastaUnpack(open('rosalind_splc.txt').read())
string = s[0][1]

for i in range(1,len(s)):
    string = string.replace(s[i][1],'')

exon = aa.stringTranslate(string.replace('T','U')).replace('#','')
print(exon)