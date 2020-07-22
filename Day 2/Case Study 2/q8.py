l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]

l3 = []
for val in l1:
    if val in l1:
        l3.append(val)
print(l3)


'''
print(
    [ val for val in l1 if val in l2]
)
'''