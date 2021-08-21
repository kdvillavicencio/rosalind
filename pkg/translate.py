map = open('.\pkg\proteinmap.txt').read()
map = map.split(sep='\n')
proteinmap = {}

for key in map:
    key = key.strip().split(' ')
    proteinmap[key[0]] = key[1]

def codonTranslate(codon):
    return proteinmap[codon]