from numpy.core.records import array
import pkg.fasta as fs
import pkg.aminoAcid as aa

s1 = open('rosalind_orf.txt').read()
s1 = fs.fastaUnpack(s1)[0][1]
s2 = s1.translate(str.maketrans('ATCG', 'TAGC'))[::-1]

rna = [s1, s1[1:-2], s1[2:-1],s2, s2[1:-2], s2[2:-1]]
arr = []

for s in rna:
    s = s.replace('T','U')
    p = aa.stringTranslate(s)
    for i in range(len(p)):
        if p[i] == 'M':
            n = p.find('#', i)
            if n != -1:
                arr.append(p[i:n])

for item in set(arr):
    print(item)
