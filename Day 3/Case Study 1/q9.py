query = str(input()).split(',')
X,Y = int(query[0]), int(query[1])
print(X , Y)
#X , Y = 3, 5
res = [[i*row for i in range(Y)] for row in range(X)]
'''
for row in range(X):
    col = [i*row for i in range(Y)]
    res.append(col)
'''     
print(res)

