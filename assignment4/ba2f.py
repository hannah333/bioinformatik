Dna = 'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
k = 8
t = 5

import random

def symtonum(x):
    return {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3,
         }[x]

def numtosym(index):
    return {
        0 : 'A',
        1 : 'C',
        2 : 'G',
        3 : 'T',
         }[index]

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

def profilemostprobable(text, k, profile):
    maxprob = 0
    kmer = text[0:k]
    for i in range(2, len(text)-k+1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            l = symtonum(pattern[j])
            prob *= profile[l][j]
        if prob > maxprob:
            maxprob = prob
            kmer = pattern
    return kmer

def createprofile(motifs):
    k = len(motifs[0])
    profile = [[1 for i in range(k)] for j in range(4)]
    for x in motifs:
        for i in range(len(x)):
            j = symtonum(x[i])
            profile[j][i] += 1
        for x in profile:
            for i in range(len(x)):
                x[i] = x[i]/len(motifs)
    return profile

def consensus(profile):
    string = ''
    for i in range(len(profile[0])):
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        string += numtosym(loc)
    return string

def score(motifs):
    profile = createprofile(motifs)
    cons = consensus(profile)
    score = 0
    for x in motifs:
        for i in range(len(x)):
            if cons[i] != x[i]:
                score += 1
    return score

def randomizedmotifsearch(Dna, k, t):
    bestmotifs = []
    motifs = []
    for x in range(t):
        random.seed()
        i = random.randint(0, len(Dna[x])-k)
        motifs.append(Dna[x][i:i+k])
    bestmotifs = motifs.copy()
    count = 0
    while True:
        profile = createprofile(motifs)
        for x in range(t):
            motifs[x] = profilemostprobable(Dna[x], k, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs.copy()
            count += 1
        else:
            print(count)
            return bestmotifs


print(randomizedmotifsearch(Dna, k, t))











