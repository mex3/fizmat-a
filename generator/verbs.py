#Берет из файла standalone.txt предложение, находит там глагол
#В файле questions-verbs.txt формирует запись следующего вида:
#Q: Петя ... погулять.
#А: Пошел
#B: Пошла
#C: Пошли
#D: Пошло
#Без символа комментария в начале строки. Тут глагол заменяется многоточием и предлагаются варианты ответа.
s=list(map(str, input().split()))
k="ooooooooooo"
for c in s:
    d=str(c[-2])+str(c[-1])
    if d=='ел' or d=='ла' or d=='ло' or d=='ли':
        k=c
        c="..."
        break
print(" ".join(s))
print("A: "+chr(ord(k[0])-32)+k[1:-2]+"ел")
print("В: "+chr(ord(k[0])-32)+k[1:-2]+"ла")
print("С: "+chr(ord(k[0])-32)+k[1:-2]+"ли")
print("D: "+chr(ord(k[0])-32)+k[1:-2]+"ло")
