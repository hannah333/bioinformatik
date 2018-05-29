text = 'ACGCGGCTCTGAAA'
k = 2

#ba1m
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

#ba1l
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

#ba1k
def ComputingFrequencies(text,k):
    FrequencyArray = [0] * (4**k)
    for r in range(0, (len(text)-k+1)):
        pattern = text [r:r+k]
        j = patonum (pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

#frequent patterns
def PatternCount(text,pattern):
    count= 0
    for i in range(0,(len(text)-len(pattern))+1):
        if text[i:i+len(pattern)]==pattern:
            count = count +1
    return count

def FasterFrequentWords (text, k):
    frequentPatterns = []
    COUNT = [0] * len(text)

    for i in range(0, (len(text) - k+1)):
        pattern = text[i: i + k]

        COUNT[i] = PatternCount(text, pattern)
    maxCount = max(COUNT)
    for i in range(0, (len(text) - k+1 )):
        if COUNT[i] == maxCount:

            if text[ i : i+k ] not in frequentPatterns:
                frequentPatterns.append( text[ i : i+k ] )
    return frequentPatterns

print(FasterFrequentWords(text,k))