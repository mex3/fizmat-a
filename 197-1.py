l = int(input())                        

x = list(map(int, input().split()))
m = []
a = list(range(l, 0, -1))
for i in range(l-1, -1, -1):
    m.append(str(a[x[i]]))
    del a[x[i]]
m.reverse()
print(' '.join(m))
