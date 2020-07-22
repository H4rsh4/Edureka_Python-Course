q = 'abcdefgabc'

qSet = sorted({i for i in q})

for var in qSet:
    print(f'{var},{q.count(var)}')
