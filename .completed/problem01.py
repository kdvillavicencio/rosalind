import pandas as pd

s = "CGTCCCGACGCGTATCGAGACGCATCTGGTTCTTTCTAGGTGTGGCCAAACGATGACGTTCAACGTCCCTGCGCGGCTACACAGCCACTTATGTACTCCCCGCACCGGGAATAGGCTAAATACTTTGTGGCCTATTCTGCCCTCGGGAGCGCTTATGCTTGTTCTAAGGTGATCGTTAGAGCAACGTTGGGCTCAGAGGTAACCTCACATCAGGCCTCACAGGATTCGGTATGAAGCTGCGCGAGCGTCTGGCTCAATTAACCGGCTGCGATTCCCCAAACAGTCGTGGGACGCTTGACCGTAGTCTGGGAGTGAAGAACTTAACTGGCTTCAAACGGCCGTTTCGCCTAACCGTCAGTTGCTCCTTACGTAAATTGGCCGCGAGTGCATAGACTATTACCGAGAAATCGACAAGAACGAATCGACCACGCAGTCACAATATCCCGTGATACCCCTCAACTTGCTAGGCGTTATTGTGCAACAGAGAGTTTTATGCATGTTTAGGTGCTGCCCTTTATCGGTGCTTCTCTCTTACTTCCGGTTTATCCGACTTCATACCCGCTCTGCTATACGCGAGCTGGTGTGGTGCTTGCTTTGAGATTATAATCACGGCTGACCCGGATTATCTATCTTGGCGGTCGCTCCAAGCCGGGAATAGATAAAAAAGATTAATTCAAAAACATGGGCGGGCGTGAGATGTTTTAAGGAGTGATGCGCATTTCAAGGATAATATCGCCCGGTAAGCGAGCCATGTCTAGAACAGTAAGGCGCGGGACACCATTGGATGCATCGGCGTGGCATGTACGCAGAGGAAAAACTCTTAATTTACA"
Acount = 0
Ccount = 0
Gcount = 0
Tcount = 0

for char in s: 
    if char=="A":
        Acount += 1
    elif char=="C":
        Ccount += 1
    elif char=="G":
        Gcount += 1
    elif char=="T":
        Tcount += 1

print(f'{Acount} {Ccount} {Gcount} {Tcount}')

# TOP SOLUTION
a = s.count("A")
c = s.count("C")
g = s.count("G")
t = s.count("T")

print(f'{a} {c} {g} {t}')