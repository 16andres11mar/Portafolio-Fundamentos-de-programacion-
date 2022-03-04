

op = 1
num1 = 0
num2 = 0
while op != 0:

    print("<1>Sumar")
    print("<2>Restar")
    print("<3>Multiplicar")
    print("<4>Dividir")
    print("<0>Salir")

    op= int(input('Ingrese una opcion:'))
    if op != 0:
        num1 = int(input('Ingrese num1:'))
        num2 = int(input('Ingrese num2:'))

    if op == 1:
        print('suma:', num1 + num2)
    elif op == 2:
        print('resta:', num1 - num2)
    elif op == 3:
        print('multiplicacion:', num1 * num2)
    elif op == 4:
        print('divicion:', num1 / num2)
    else:
        print('No existe la opcion')