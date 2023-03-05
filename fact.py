def fun(n):
    if n<=0:
        return
    return n*fun(n-1)

fun(3)