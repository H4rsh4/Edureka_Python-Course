q = '10,110,0101,0110,1100'
t = [i for i in [bin(i) for i in q.split(',')] if int(i)%5==0]
print(','.join(t))