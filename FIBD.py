input = open('rosalind_fibd.txt').read().split(sep=' ')

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
