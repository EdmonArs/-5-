storona_kvadrata = int(input("Введите сторону квадрата: "))

perimetr = storona_kvadrata * 4
S = storona_kvadrata**2
diagonal = (storona_kvadrata**2 + storona_kvadrata**2)**0.5
print("Периметр квадрата: ", perimetr )
print("Площадь квадрата: ", S )
print("диагональ квадрата:", round(diagonal, 3))


#простейший калькулятор
oper = input("Введите операцию(+, -, *, /) ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if oper == '+':
  print(a + b)
if oper == '-':
  print(a - b)
if oper == '*':
  print(a * b)
if oper == '/':
  print(a / b)