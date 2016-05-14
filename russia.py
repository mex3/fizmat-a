import random

strany = open('russia.txt', 'r')
spis = {}
stra = []
i = 0
a = strany.readline()
print('Если Вы хотите закончить проверку, Вы можете написать слово \'stop\'.')
print('Предупреждение!! Писать только маленькие английские буквы.')
print('Пишите столицы или центры республик, автономных округов и областей, краёв России.')
while a!='':
    b, c = map(str, a.split())
    spis[b]=c
    stra.append(b)
    i+=1
    a = strany.readline()
w = 0
l = 36
q = l
u = []
while q>0:
    a = random.randint(0, i-1)
    while a in u:
        a = random.randint(0, i-1)
    u.append(a)
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
        break
    if f==x:
        print('Правильно!\n')
        w+=1
    else:
        print('Неправильно!')
        print(f+') '+spis[z]+'\n')
    q-=1
try:
    _=int(w/(l-q)*100)
except ZeroDivisionError:
    _=0
print('Ваш результат - '+str(w)+'/'+str(l-q)+'.')
print('Это '+str(_)+'%.')
print('Ваша оценка - ', end='')
if _<50:
    print(2, end='.\n')
elif _<70:
    print(3, end='.\n')
elif _<85:
    print(4, end='.\n')
else:
    print(5, end='.\n')
strany.close()