import random

strany = open('strany.txt', 'r')
spis = {}
stra = []
i = 0
a = strany.readline()
print('If you want to close the program, you can write \'stop\'.')
print('Warning!! Please, you could write only little letters.')
while a!='':
    b, c = map(str, a.split())
    spis[b]=c
    stra.append(b)
    i+=1
    a = strany.readline()
w = 0
l = 25
q = l
while q>0:
    a = random.randint(0, i-1)
    z = stra[a]
    print(z+':')
#-------------------------------------------------------------------------------
    d = random.randint(0, 3)
    f = chr(d+97)
    r = [a]
    for _ in range(4):
        print(chr(_+97)+') ', end='')
        if d==_:
            print(spis[z])
        else:
            while True:
                e = random.randint(0, i-1)
                if e not in r:
                    r.append(e)
                    break
            print(spis[stra[e]])
#-------------------------------------------------------------------------------
    x = input()
    if x=='stop':
        print('Do you really want to close the program?')
        x = input()
        if x=='yes':
            break
        else:
            continue
    if f==x:
        print('True!')
        w+=1
    else:
        print('False!')
        print(f+') '+spis[z])
    i-=1
    del spis[z]
    q-=1
_=int(w/(l-q)*100)
print('Your result is '+str(w)+'/'+str(l-q)+'.')
print('It\'s '+str(_)+'%.')
print('Your mark is ', end='')
if _<50:
    print(2, end='.\n')
elif _<70:
    print(3, end='.\n')
elif _<85:
    print(4, end='.\n')
else:
    print(5, end='.\n')
strany.close()