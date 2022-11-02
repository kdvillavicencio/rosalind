import pkg.fasta as fs

sList = fs.fastaUnpack(open('rosalind_grph.txt').read())
k = 3

#print(sList[1][1][-k:])

for s in sList:
    for i in range(len(sList)):
        if s[1] != sList[i][1]:
            if s[1][0:k] == sList[i][1][-k:]:
                print(sList[i][0]+' '+s[0])