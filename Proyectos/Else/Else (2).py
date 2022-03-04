
print ("Ingrese fecha")
año=int(input("Introduzca el año:"))
mes=int(input("Introduzca el mes:"))
dia=int(input("Introduzca el dia:"))

if año>0:
    #año=True
    print("año correcto",año)
else:
    #año=False 
    print("año incorrecto",año)    
if año%4==0 and  año%100!=0 or año%400==0:
    bisciesto= True   
else:
    bisciesto= False

if mes>=1 and mes<=12: 
    #mes=True
    print("mes correcto",mes)
else:
    #mes=False
    print("mes incorrecto",mes)
    if mes in(1,3,5,7,8,10,12):
        dias_mes=31
        if dia<=31 and dia>=1:
            print("dia correcto",dia)   
        else:
            print("dia incorrecto",dia)
    elif mes==2:
        if bisciesto:
            dias_mes=29
        else:
            dias_mes=28
    else:
        dias_mes=30
if (dia<=31 and dia>=1) and (dia<=29 and dia>=1) and (dia<=30 and dia>=1) and (dia<=28 and dia>=1):
    print("dia correcto",dia)   
else:
    print("dia incorrecto",dia)    
    
print("La fecha es:",año,"/",mes,"/",dia)
#if dia<=31 and dia>=1:
    #dia=True
    #print("dia correcto",dia)
#else:
    #dia= False
    #print("dia incorrecto",dia)


#print("fecha incorrecta")
#print('hoy es',dia, "el mes actual es",mes, "el año es", año)
