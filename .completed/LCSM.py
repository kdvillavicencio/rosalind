import pkg.fasta as fs

sList = fs.fastaUnpack(open('rosalind_lcsm.txt').read())

common = []
for i in range(len(sList[0][1])):
    for j in range(i+2,len(sList[0][1])+1):
        a = 0
        for s in sList:
            if sList[0][1][i:j] in s[1]:
                a += 1
        if a == len(sList) and len(common) < len(sList[0][1][i:j]):
            common = sList[0][1][i:j]
            print(sList[0][1][i:j])

