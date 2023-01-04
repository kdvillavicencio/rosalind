'''
n = [21,13,19,3,11,5,18]
n.sort()
print(n[len(n)//2])
print(n)
'''

'''
intList = [3, 2]
outList = []
space = ' '
outList.append(space.join(str(i) for i in intList))
outList.append(space.join(str(i) for i in intList[::-1]))
print(outList)
'''

intList = [[3, 2],[4,4]]
intList.append(intList[::][::-1])

print(intList)