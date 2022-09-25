def factoriall(s):
    t = 1
    if s ==0:
        return 1
    else:
        return s * factoriall(s-1)
print(factoriall(5))
