import pandas as pd

# P(parent1) * P(parent2) * P(base)
input = open('rosalind_iprb.txt').read()
input = input.split(sep=' ')
k = float(input[0])
m = float(input[1])
n = float(input[2])
tot = k + m + n

base = pd.DataFrame([[1.0, 1.0, 1.0], [1.0, 0.75, 0.5], [1.0, 0.5, 0]])
prob = pd.DataFrame([[k*(k-1), k*m, k*n],[m*k, m*(m-1), m*n],[n*k, n*m, n*(n-1)]])
resultdf = prob*base.values
result = resultdf.to_numpy().sum()/(tot*(tot-1))

print(result)
