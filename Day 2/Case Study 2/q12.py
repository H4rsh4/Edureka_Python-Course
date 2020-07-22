n = int(input('>'))
'''
res = 0

for f in range(1, n+1):
    res += f/(f+1)
    
print(res)
'''

print(round(
            sum(
                [ i/(i+1) for i in range(1, n+1) ]
            ),
            2
        )
)