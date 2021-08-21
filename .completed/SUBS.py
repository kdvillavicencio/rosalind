st = open('rosalind_subs.txt').read().split(sep='\n')
s = st[0]
t = st[1]
loc = ''

for i in range(len(s)):
    if s[i:i+len(t)] == t:
        loc = loc + str(i + 1) + ' '

print(loc)
