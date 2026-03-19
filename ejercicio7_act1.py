usuario = input("Escriba pues ")

palabras = usuario.split()

lista_palabras = []

for p in palabras:
    if len(p) > 3:
        lista_palabras.append(p)

oracion = " ".join(lista_palabras)
print(f"Resultado: {oracion}")