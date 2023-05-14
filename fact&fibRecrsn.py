"""
def fib(n):
    if n<0:
        return None
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(6))
"""
def fact(n):
    if n<0:
        return None
    if n<2:
        return 1
    return n*fact(n-1)
print(fact(6))