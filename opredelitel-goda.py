#определение високосный ли год
year = int(input('Введите год: '))
if year % 4 == 0:
  print('Год високосный')
else:
  print('Год не високосный')


#определитель високосных годов в диапазоне

a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))

for i in range(a, b+1):
  if i % 4 == 0:
    print(i)