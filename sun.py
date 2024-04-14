def ravi(a):
    if a==0:
        return 1
    else:
        return a*ravi(a-1)
print(ravi(6))