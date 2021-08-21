sample = "AAAACCCGGT"

s = open("rosalind_revc.txt").read()
c = s[::-1].strip()
sc = ""
map = {"A":"T", "T":"A", "G":"C", "C":"G"}
for i in c:
   sc+=str(map[i])

print(sc)

# TOP SOLUTION
# 1. replace using lowercase!
# 2. use `maketrans()` map then translate()
