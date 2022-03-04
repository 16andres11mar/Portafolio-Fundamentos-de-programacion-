# Calcular el mayor de cuatro numeros enteros introducidos por teclado
num1= 11
num2= 16
num3= 31
num4= 1
num5= 7
if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num1 < num4:
    num1, num4 = num4, num1

if num1 < num5:
    num1, num5 = num5, num1

if num2 < num3:
    num2, num3 = num3, num2

if num2 < num4:
    num2, num4 = num4, num2

if num2 < num5:
    num2, num5 = num5, num2

if num3 < num4:
    num3, num4 = num4, num3

if num3 < num5:
    num3, num5 = num5, num3

if num4 < num5:
    num4, num5 = num5, num4
print("a:", num1)
print("b:", num2)
print("c:", num3)
print("d:", num4)
print("e:", num5)