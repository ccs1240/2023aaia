a = int(input())

b=a%10
c=a//10%10
d=a//100%10
c=a//a//1000%10

print(b*1+c*2+d*4+c*8)