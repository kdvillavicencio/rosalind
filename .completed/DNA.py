s = open('rosalind_dna.txt').read()
a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')

print(f'{a} {c} {g} {t}')