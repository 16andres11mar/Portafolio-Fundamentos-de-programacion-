import random

op = -1
juego = -1 
empates=0
ganados=0
perdidos=0

def menu ():
    print("<1> jugar")
    print("<2> resultados")
    print("<3> salir")    
while op != 0:
        menu ()
        op = int(input("ingrese una opcion: "))
        if op == 1:
            while juego != 4:
                print("<1> piedra")
                print("<2> papel")
                print("<3> tijera")
                print('<4> regresar')
                juego = int(input("ingrese su eleccion: "))
                if juego == 4:
                    menu()
                num = random.randint(1,3)
                if juego== num:
                    print ("Empate", juego, "vs", num)
                    empates+=1
                elif juego==1:
                    if num==2:
                        print ("pierdo", juego, "vs", num)
                        perdidos+=1
                    elif num ==3:
                        print ("gano", juego, "vs", num)
                    ganados+=1
                elif juego==2:
                    if num==1:
                        print ("gano", juego, "vs", num)
                        ganados+=1
                    elif num==3:
                        print ("pierdo", juego, "vs", num)
                    perdidos+=1
                elif juego==3:
                    if num==1:
                        print ("pierdo", juego, "vs", num)
                        perdidos+=1
                    elif num==2:
                        print ("gano", juego, "vs", num)
                    ganados+=1
                else:
                    print("ingrese una opcion correcta")
        elif op == 2:
            print("ganados: ",ganados)
            print("perdidos: ", perdidos)
            print("empatados: ",empates)
        elif op == 3:
            quit()
        else:
            print("ingrese una opcion correcta")