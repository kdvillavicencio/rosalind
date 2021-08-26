import pkg.aminoAcid as aa

s = open('rosalind_mrna.txt').read().replace('\n','')
count = aa.codonProbability('Stop')
n = 1000000.0
mod = 1.0
'''
for i in s:
    count *= aa.codonProbability(i)
    if count > n:
        mod = mod + count - n
        count = 1.0
    if mod > n:
        mod = mod - n

for i in s:
    count *= aa.codonProbability(i)
    if count > n:
        mod = mod * (count - n)
        count = 1.0
    if mod > n:
        mod = mod % n
'''
for i in s:
    count = (count%n) * aa.codonProbability(i)

mod = count%n
print(mod)
