#input = open('./pkg/test_fasta.txt').read()

def fastaUnpack(input):
    s = input.split(sep='>')
    s.remove("")

    output = []
    for i in s:
        arr = i.split(sep='\n', maxsplit=1)
        arr[1] = arr[1].replace('\n', '')
        output.append(arr)

    return output

#print(fastaUnpack(input))
