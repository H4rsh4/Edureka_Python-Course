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
    result = float(0)
    for f in ite:
        result+=f
    return result