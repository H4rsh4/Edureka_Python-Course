"""
Obj:
    Write a program which will find factors of given number and find whether the factor is even or odd.
"""

query = int(input('>'))

factors = []

#Checking each number in the range for its divisibility and Even/Odd nature
for num in range(query+1):
    if query%num == 0 and num%2==0:
        print(num, ": Even Factor")
    elif query%num == 0 and num%2!=0:
        print(num, ": Odd Factor")
