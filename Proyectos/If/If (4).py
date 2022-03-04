#Dada la fecha de hoy
#Calcular la fecha del #dia siguiente
#Suponer que el año no es #bisiesto

print ("Ingresar la fecha")
año=int(input("Introducir el año: "))
mes=int(input("Introducir el mes: "))
dia=int(input("Introducir el dia: "))

if año%4==0 and  año%100!=0 or año%400==0:
    bisciesto= True   
else:
    bisciesto= False

if mes in (1, 3, 5, 7, 8, 10, 12):
    dias_mes = 31
elif mes == 2:
    if bisciesto:
        dias_mes = 29
    else:
        dias_mes = 28
else:
    dias_mes = 30

if dia < dias_mes:
    dia += 1
else:
    dia = 1
    if mes == 12:
        mes = 1
        año += 1
    else:
        mes += 1

print("año",año,"/ mes",mes,"/ dia",dia)