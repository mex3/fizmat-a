def IsPrime(n):
	import math
	a = [True] * n
	for i in range(2, int(math.sqrt(n))+1):
		for j in range(i * 2, n, i):
			a[j] = False
	b = [i for i in range(2, n) if a[i]]
	if n-1 in b:
		return True
	else:
		return False
	
n = int(input()) + 1
q = IsPrime(n)
if q:
	print('YES')
else:
	print('NO')