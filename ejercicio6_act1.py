numero = int(input(" Ingrese número elegido "))

lista_multiplos5 = []
lista_resto = []

for i in range (1, numero+1):
    if i % 5 == 0:
        lista_multiplos5.append(i)
    else:
        lista_resto.append(i)
        
print(f"La lista de multiplos de 5 es: {lista_multiplos5}")
print(f"La lista del resto de los números es: {lista_resto}")