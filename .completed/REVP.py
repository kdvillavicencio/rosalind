from tarfile import LENGTH_NAME
import pkg.fasta as fasta
import pkg.functions as fx

# 1. Complement
# 2. Reverse
# 3. Find duplicates

s = open('rosalind_revp.txt').read()
s1 = fasta.fastaUnpack(s)[0][1]
print(s1)

for i in range(len(s1)+1):
    for length in range(4,13):
        if i <= len(s1)-length:
            if s1[i:i+length] == fx.Reverse(fx.Complement(s1[i:i+length])):    
                print(f"{i+1} {length}")
