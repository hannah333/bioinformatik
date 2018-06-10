Dna = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
k = 3

def HammingDistance(str1, str2):
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs


def DistanceBetweenPatternAndStrings(Pattern,Dna):
    k = len(Pattern)
    distance = 0
    for texts in Dna:
        HammingD = float('inf')
        for i in range (0, (len(texts)-k+1)):
            if HammingD > HammingDistance(Pattern,texts[i:i+k]):
                HammingD = HammingDistance(Pattern, texts[i:i+k])
        distance = distance + HammingD
    return distance

def numtopat (index,k):
    if k == 1:
        return numtosym(index)

    prefixindex = index // 4
    t = index % 4
    sym = numtosym(t)
    prefixpattern = numtopat(prefixindex, k-1)

    return prefixpattern + sym

def numtosym(index):
    return {
        0 : 'A',
        1 : 'C',
        2 : 'G',
        3 : 'T',
         }[index]

def MedianString(Dna,k):
    distance = float("inf")
    Median = ''
    for i in range (0, (4**k)-1):
        Pattern = numtopat (i,k)
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    return Median

print(MedianString(Dna,k))
