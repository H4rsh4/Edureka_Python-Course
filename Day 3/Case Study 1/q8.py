q = [int(i) for i in "100,150,180".split(',')]
C = 50 
H = 30
print(q)
res = [ str(  int(  ( (2*C*D)/H )**(1/2)  )   ) for D in q ]
print(','.join(res))