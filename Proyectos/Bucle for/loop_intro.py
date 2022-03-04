# El ciclo for ejecuta un bloque de codigo repetidamente hasta que la condicion en el ciclo for no ses valida
# ejemplo

mascotas = ['gatos', 'perros', 'gatos', 'peces', 'perros', 'perros']

for i in mascotas:
    print(i)
# Con contador se define la lista y ya en la parte de abajo se inica con contador con 0 para q #
# mas adelante pueda sacar un total para contar
#contador = 0

#for i in mascotas:
#    if i == "gatos":
#        contador = contador + 1
        
#print("El total de gatos es:", contador)
# lo de arrriba primera forma de contar
# segunda forma


contador_gatos = 0
contador_perros = 0
contador_peces = 0

for i in mascotas:
    if i == 'gatos':
        contador_gatos = contador_gatos + 1
    elif i == 'perros':
        contador_perros = contador_perros + 1
    elif i == 'peces':
        contador_peces= contador_peces + 1

print("El numero de gatos es:", contador_gatos)
print("El numero de perros es:", contador_perros)
print("El numero de peces es:", contador_peces)
