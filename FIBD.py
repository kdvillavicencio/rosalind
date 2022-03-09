import pkg.aminoAcid as aa

input = open('rosalind_fibd.txt').read().split(sep=' ')

# MORTAL FIBONACCI RABBITS
# Total Rabbits: Fibonacci Series Fn = F(n-1) + F(n-2)
# Dead Rabbits: D(n) = SUM(F(0) ~ F(n-3)))

def rabbit(n, k, m):    
    pairAdult = [0.0, 1.0]
    for x in range(n):
        if x - m + 1 < 0:
            death = 0.0
        else:
            death = pairAdult[x - m + 2]
        pairAdult.append(pairAdult[x+1] + k*pairAdult[x] - death)

    return pairAdult[n+1]

print(rabbit(int(input[0]), 1, int(input[1])))

# i = 0: 0
# if i = 1: 1
# if i = 2: 0 + 1 = 1   x2 = x1 + x0
# if i = 3: 1 + 1 = 2   x3 = x2 + x1 - x0
# if i = 4: 2 + 1 = 3   x4 = x3 + x2 - x2
# if i = 5: 3 + 2 = 5   x5 = x4 + x3 - x2 - x1
# if i = 6: 5 + 3 = 8   x6 = x5 + x4 - x3 - x2 - x1
