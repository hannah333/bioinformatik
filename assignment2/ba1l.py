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

    print (x)

patonum('AGT')

