n = 8
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
print(factorial(n))