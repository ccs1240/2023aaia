a=list(map(int,input().split()))
a.sort()

for i in range(9,-1,-1):
	print(a[i],end=' ')