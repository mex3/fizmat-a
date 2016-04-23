#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
n = int(input()) + 1
# Выписать подряд все целые числа от 2 до n (2, 3, 4, …, n).
a = [True] * n
# Берëм невычеркнутые числа от 2 до sqrt(n)
for i in range(2, int(math.sqrt(n))+1):
	# Вычëркиваем числа, кратные невычеркнутому
	for j in range(i * 2, n, i):
		a[j] = False
# Все невычеркнутые числа - простые
b = [i for i in range(2, n) if a[i]]


if n-1 in b:
	print('YES')
else:
	print('NO')
