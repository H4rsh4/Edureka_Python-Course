q = 'Hello world!'

firstLetter = [i for i in q if i.isalnum() ]

lCase = len([i for i in firstLetter if not i.isupper() ])
uCase = len([i for i in firstLetter if i.isupper() ])

print(f'UPPER CASE {uCase}\nLOWER CASE {lCase}')
