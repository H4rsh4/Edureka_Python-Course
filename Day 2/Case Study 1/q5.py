q = str(input('>'))
print( True if q == ''.join( [i for i in q][::-1] ) else False)