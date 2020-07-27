#SUM
def summ(ite):
    '''
    Return the sum of an iterable
    '''
    result = 0
    for f in ite:
        result+=f
    return result

def fsumm(ite):
    result = 0
    for f in ite:
        result+=f
    return round(result,1)

print(summ([.2, .2, .2, .2, .2, .2, .2, .2, .2, .2]))
print(fsumm([.2, .2, .2, .2, .2, .2, .2, .2, .2, .2]))



'''
An Implementation of fsum using intermediate partial sums
sourced from:https://code.activestate.com/recipes/393090/

def msum(iterable):
    "Full precision summation using multiple floats for intermediate values"
    # Rounded x+y stored in hi with the round-off stored in lo.  Together
    # hi+lo are exactly equal to x+y.  The inner loop applies hi/lo summation
    # to each partial so that the list of partial sums remains exact.
    # Depends on IEEE-754 arithmetic guarantees.  See proof of correctness at:
    # www-2.cs.cmu.edu/afs/cs/project/quake/public/papers/robust-arithmetic.ps

    partials = []               # sorted, non-overlapping partial sums
    for x in iterable:
        i = 0
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    print(partials)
                        
    return sum(partials, 0.0)
print(msum([.2, .2, .2, .2, .2, .2, .2, .2, .2, .2]))

'''