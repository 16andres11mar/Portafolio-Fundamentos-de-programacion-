
# Calcular el promedio de un alumno que tiene 7 calificaiones en la materia de calculo



n= 7
suma= 0
for i in range(n):
    nota= int(input('Ingrese nota:' + str(i) + ':' ))
    suma += nota 

promedio= suma / n

print('Promedio:', promedio)