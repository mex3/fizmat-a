a, b = map(int, input().split())
d=[]
for c in range(a):
    s=sum(list(map(int, input().split())))
    d.append(s)
maxi=d[0]
for c in d:
    if c>maxi:
        maxi=c
print(maxi)
print(d.index(maxi))