index = 45
k = 4

def numtosym(index):
    return {
        0 : 'A',
        1 : 'C',
        2 : 'G',
        3 : 'T',
         }[index]

def numtopat (index,k):
    if k == 1:
        return numtosym(index)

    prefixindex = index // 4
    t = index % 4
    sym = numtosym(t)
    prefixpattern = numtopat(prefixindex, k-1)

    return prefixpattern + sym

print(numtopat(index,k))
