text = 'ACGCGGCTCTGAAA'
k = 2

def symtonum(x):
    return {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3,
         }[x]

def patonum (pattern):
    k = len(pattern)
    x=0
    i=1

    while i<=(k):
        x = x + symtonum(pattern[k-i])*(4**(i-1))
        i=i+1
    return x
  # print (x)


def ComputingFrequencies(text,k):
    FrequencyArray = [0] * (4**k)
    for r in range(0, (len(text)-k+1)):
        pattern = text [r:r+k]
        j = patonum (pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

print(ComputingFrequencies(text,k))
