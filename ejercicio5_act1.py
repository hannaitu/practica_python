total_acumulado = 0

while True:
    precio = float(input(" Ingrese el precio del producto "))
    
    if precio == 0:
        break

    total_acumulado = total_acumulado + precio

print(f"El total es: ${total_acumulado}")