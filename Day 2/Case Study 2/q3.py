import string

'''
criteria:
    1 a-z
    1 0-9
    1 $#@
    min len : 6
    max len : 12
'''

alphabets = [i for i in string.ascii_lowercase]
digits = [i for i in range(0,10)]
splchar = ['$','#','@']

pwd = str(input())
passCondition = True
flags = [
    any([alp in pwd for alp in alphabets ]),
    any([str(dig) in pwd for dig in digits ]),
    any([alp in pwd for alp in splchar ]),
]

for flag in flags:
    if flag is False:
        cond = False
        break
if passCondition and 5<len(pwd)<13:
    print("Good Password!")
else:
    print("Bad Password")
    


