res = []
for num in range(1000, 3001):
    digits = [i for i in str(num)]
    flag = True
    for dig in digits:
        if int(dig)%2 != 0:
            flag = False
    if flag == True:
        res.append(num)
#print(res)



