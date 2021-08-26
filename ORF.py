from numpy.core.records import array
import pkg.fasta as fs
import pkg.aminoAcid as aa

s = open('sample.txt').read()
s = fs.fastaUnpack(s)[0][1]
s = s.replace('T','U')
print(len(s))
p = aa.stringTranslate(s)
print(p)
arr = []

i = 0
while i > -1:
    m = p.find('M',i)
    n = p.find('#', m)
    i = n
    if i == -1:
        break
    arr.append([p[m:n]])


print(arr)
