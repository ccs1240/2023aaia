a=[1, 3, 5, 7, 9]
for i in range(5):
  print('i是', i, '這時a[i]的值是',a[i])a = [1,3,5,7,9,11,13,15,19]
N = len(a)
for i in range (N-1):
  print('現在的i是', i, 'a[i]是',a[i], 'a[i+1]', a[i+1], '相減是', a[i+1-a[i]])