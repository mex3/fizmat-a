a, b = map(int, input().split())
d=[]
e=[]
for c in range(a):
    i=list(map(int, input().split()))
    d.append(max(i))
print(d.count(max(d)))
