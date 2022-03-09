
def Complement(input):
    output = input.replace('A', 'X').replace('T', 'A').replace('X','T').replace('C', 'Y').replace('G', 'C').replace('Y', 'G')
    return output

def Reverse(input):
    output = input[::-1]
    return output

#test = 'TCAATGCATGCGGGTCTATATGCAT'
#print(Reverse(test))
