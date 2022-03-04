#Determinar en que estado está el agua en función de su temperatura. 
# Si es negativa el estado será sólido, si es menor que 100 será líquido y si es mayor que 100 será gas. 
# Pedir al usuario el valor de la temperatura.


temperatura=int(input("Ingrese la temperatura:"))
if(temperatura <= 0):
    print("El estado es solido")

elif(temperatura > 0 and temperatura <= 100):
    print("El estado es liquido")

else:
    print("El estado es gaseoso")