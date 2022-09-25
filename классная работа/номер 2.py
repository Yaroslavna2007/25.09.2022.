a = int(input())
d = int(input())
c = int(input())
def max(a, d):
    if a>d:
        return a
    else:
        return d
def max2(a,d,c):
    if max(a,d)>c:
        print(max(a,d))
        return max(a,d)
    else:
        print(c)
        return c
max2(a, d, c)