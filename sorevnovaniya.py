a, b = map(int, input().split())
d=[]
e=[]
for c in range(a):
    i=list(map(int, input().split()))
    s=max(i)
    e.append(i.index(s))
    d.append(s)
maxi=d[0]
for c in d:
    if c>maxi:
        maxi=c
print(maxi)
print(d.index(maxi), e[d.index(maxi)])