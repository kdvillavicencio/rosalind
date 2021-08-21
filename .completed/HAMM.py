
st = open('rosalind_hamm.txt').read().split(sep='%')
[s,t] = st
dh = 0

for i in range(len(s)):
    if s[i] != t[i]:
        dh += 1

print(dh)
