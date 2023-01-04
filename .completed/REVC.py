import pkg.functions as fn

s = open('rosalind_revc.txt').read()
sc = fn.Complement(fn.Reverse(s))
print(sc)