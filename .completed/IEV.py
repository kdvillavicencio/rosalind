input = open('rosalind_iev.txt').read().split(sep=' ')
map = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
totDom = 0.0
total = 0.0
for i in range(len(input)):
    Dom = float(input[i]) * 2 * map[i]
    totDom += Dom
    total += float(input[i])

print(totDom)