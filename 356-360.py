#http://informatics.mccme.ru/mod/statements/view.php?id=15232#1
#СЂРµС€РёС‚СЊ РЅРµСЃРєРѕР»СЊРєРѕ Р·Р°РґР°С‡ РёР· 5
s = list(map(int, input().split()))
m = s[0]
n = s[1]
A = [0] * m
i = 0
for i in range(m):
    A[i] = [0] * n
#конструкция создаёт массив из нулей в котором m строк и n столбцов