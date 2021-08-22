import pkg.aminoAcid as aa

s = open('rosalind_mrna.txt').read().replace('\n','')
count = aa.codonProbability('Stop')
n = 1000000
mod = 0.0

for i in s:
    count *= aa.codonProbability(i)
    if count > n:
        mod = mod + count - n
        count = 1.0
    if mod > n:
        mod = mod - n
            
print(mod)
