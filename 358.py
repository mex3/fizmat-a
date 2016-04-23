a, b = map(int, input().split())
d=[]
e=[]

for c in range(a):
    i=list(map(int, input().split()))
    e.append(sum(i))
    d.append(max(i))
if d.count(max(d))==1:
    print(d.index(max(d)))
else:
    maximu=e[d.index(max(d))]
    i=[]
    u=[]
    for c in range(len(d)) :
        if d[c]==max(d):
            i.append(e[c])
            u.append(c)
    print(u[i.index(max(i))])
