
from math import factorial

input = 5
ints = [*range(1,input+1)]
perms = []

# solved by using .copy() method, previous problem on original list being overwritten

def perm(intList):
    ref_intList = intList.copy()
    outList = []
    if len(ref_intList) == 2:
        space = ' '
        outList.append(space.join(str(i) for i in ref_intList))
        outList.append(space.join(str(i) for i in ref_intList[::-1]))
        return outList
    else:
        for i in ref_intList:
            sub_intList = ref_intList.copy()
            sub_intList.remove(i)
            sub_permList = perm(sub_intList)
            for j in sub_permList:
                outList.append(str(i)+' '+j)
        return outList

perms = perm(ints)

print(factorial(input))
for item in perms:
    print(item)

