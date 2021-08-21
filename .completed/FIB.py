
s = open('rosalind_fib.txt').read()
print(s)
var = s.split(sep=' ')

def rabbit(n, k):    
    pair = [0.0, 1.0]
    for x in range(n):
        #print(x)
        pair.append(pair[x+1] + k*pair[x])
    return pair[n]

print(rabbit(int(var[0]), float(var[1])))
