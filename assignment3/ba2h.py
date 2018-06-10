Pattern = 'AAA'
Dna = ['TTACCTTAAC','GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']


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



print(DistanceBetweenPatternAndStrings(Pattern, Dna))