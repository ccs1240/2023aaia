#剝皮法
a = 1234
ans = 0 #答案要把你撥下來的皮慢慢塞進去
while a>0:
  ans = ans * 10 + a%10
  print('現在的a是', a, '撥出來的皮a%10是', a%10, '現在的ans就變成', ans)
  a = a // 10