def fun(s):
    return len(s)
l=["gfg","courses","python"]
l.sort(key=fun)
print(l)
l.sort(key=fun,reverse=True)
print(l)