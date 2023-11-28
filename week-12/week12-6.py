def ged(a,b):
	if a==0: return b
	if b==0: return a
	return ged(b, a%b)



a,b = list(map(int,input().split()))

if a<0: a=-a
if b<0: b=-b

print( ged (a,b),end='')
