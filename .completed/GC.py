import pandas as pd

s = open("rosalind_gc.txt").read()
#s = open("sample.txt").read()
#s = pd.read_text("sample.txt")

def dnaGC(dna):
    dna2 = dna.replace('\n','')
    print(len(dna2))
    return (dna2.count("C")+dna2.count("G"))/(len(dna2))*100

data = pd.DataFrame(columns=['string','GC'])
dataset = s.split(sep=">")
dataset.remove("")

for item in dataset:
    df = pd.DataFrame([[item[14:],dnaGC(item[14:])]],columns=['string','GC'],index=[item[0:13]])
    data = data.append(df)

print(data.head())
print(data['GC'].idxmax())
print(data['GC'].max())

