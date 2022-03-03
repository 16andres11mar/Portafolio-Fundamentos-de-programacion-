# Portafolio-de-fundamentos-de-programaci-n
# Qué es Python?
Python es un lenguaje de programación interpretado,sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites

# Qué es una variable?
Una variable se declara para indicarle al programa a partir de qué lugar empieza a existir, qué nombre tendrá y qué tipo de datos almacenará,es un elemento que se emplea para almacenar y hacer referencia a otro valor o para explicarlo de una manera mas sencilla es una caja que guarda zapatos, la caja es la varuable y los zapatos el valor a asginar.

## Nombrando una variable
La creación de variables se realiza a través de la asignación de un valor a la misma.
El operador de asignación en Python es el “=“
* x = 100                                                      
De derecha a izquierda                                      
"correcto"  
* 100 = x                                                      
De izquierda a derecha                                      
"incorrecto" 

## Asignando valores a una variable
* Asignación en la misma línea:
  * x = 5; y = 9; z = 12
* Asignación múltiple:
  * day, month, year = “miércoles”,”mayo”, 2016
* Asignación del mismo valor:
  * largo = ancho = 4
* Asignación de intercambio:
  * base = 15; altura = 30
  * base, altura = altura, base


## Operadores básicos
* suma (+)
* resta (-)
* multiplicacion (*)
* division (/)
* division euclidiana (cociente)(//)
* módulo (%)
* potencia (** )

### Ingreso y salida
input:Esta función permite obtener el texto escrito por el usuario, el cual se asignará a un espacio de memoria con el nombre que el programador vea conveniente.
```python
#Entrada
num=int(input("ingrese un numero:"))
```

print:sirve para mostrar un mensaje en la pantalla de una aplicación de consola
```python
#Salida
print("El numero es:",num)
```


### Suma
La suma se realiza uniendo el valor de 2 o más numeros (+)
```python
#Aqui ya se le asigna valor a las variables
 num1=6
 num2=10
 sum1=num1+num2
 print(num1,'-',num2,'=',sum1)
```

```python
#Aqui se debe ingresar valor a los numeros por consola
 num1int(input("ingrese un numero:"))
 num2=int(input("ingrese un numero:"))
 sum1=num1+num2
 print(num1,'-',num2,'=',sum1)
```

### Resta
La resta se realiza quitando valores entre 2 o mas numeros 
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
resta=num1-num2
print(num1,'-',num2,'=',resta)
```

```python
#Aqui se debe ingresar valor a los numeros por consola
num1int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
resta=num1-num2
print(num1,'-',num2,'=',resta)
```

### Multiplicación
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
mult=num1*num2
print(num1,'*',num2,'=',mult)
```

```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
mult=num1*num2
print(num1,'*',num2,'=',mult)
```

### División
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
divi=num1/num2
print(num1,'/',num2,'=',divi)
```

```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
divi=num1/num2
print(num1,'/',num2,'=',divi)
```

### Módulo
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```

```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```


# Tipos de datos en Python
Los tipos de datos serían:
* Numeros enteros
* Numeros de punto flotante
*  Texto (cadenas de caracteres)
*  Booleanos (Verdadero y falso)

## Casting en Python
 El casting es la tecnica que sirve para convertir un dato de un tipo a un tipo de dato diferente
 ```python
   int a str: str(45)
   str a int: int ("123")
   float a int: int (3.5)
```

## Integer
```python
dia="lunes"
print(type(dia))
```

## Float
```python
dia=21
print(type(dia))
```

## String
```python
dia=21.5
print(type(dia))
```

## List
Una lista es una estructura de datos en Python que es una secuencia de elementos ordenados mutables o cambiables. Cada elemento o valor que está dentro de una lista se denomina elemento. Así como las cadenas se definen como caracteres entre comillas, las listas se definen con valores entre corchetes [ ]
```python
list_1 = [ 1,6,9]
print(list_1)

list_2 = [ 5,6]
print(list_2)
```

## Tuple
Una tupla es una colección de objetos de Python separados por comas. De alguna manera, una tupla es similar a una lista en términos de indexación, objetos anidados y repetición, pero una tupla es inmutable a diferencia de las listas que son mutables.
```python
()
(1,2,4,5,6,7,8,9)
("Hola", "me", "llamo","Brando")

```

## Dictionary
Palabras reservadas
```python
 and assert break class continue def del elif
else except exec finally for from global if
import in input is lambda next not or pass
print raise return try while yield 
```
# Tomando decisiones
* Las palabras vlave if,elif,else permieten dirigir el camino por el que va a avanzar el programa dependiendo de una o varias condiciones
- Luego de los dos puntos(:), dejamos 4 espacios de sangria en la siguiente linea o una tabulación

## Sentencia if
```python
#Escribir un programa que solicite un valor entero al usuario
#determine si es par o impar
num=int(input("ingrese numero:"))


if (num%2==0):
    print("El numero es par",)
    print(num,"es par")
else:
    print("El numero es impar")  
```


## Ciclo For
```python
# Calcular la suma y la media aritmetica de Nnumeros reales. 
# solicitar el valor de n al usuario y cada uno de los N números reales.

n = int(input("Ingrese los números que desee: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
```

## Ciclo While
```python
#10-20

num=11

while num<10 or num >20 or num%2!=0:
    num=int(input("ingrese numero:"))

print("se fue")
```

## Break
```python
j=0
for i in range (10):
    j+=2
    print ("i;",i,"j:",j)
    if j==10:
        break
```

## Continue
```python
contador=0
for i in range (10):
    for j in range (10):
        contador +=1
        print ("i:",i,"j:",j)
        if contador >50:
            continue
print ("contador:",contador)
```
