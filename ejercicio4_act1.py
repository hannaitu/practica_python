numero = int(input(" Ingrese número elegido "))

for i in range (1, numero+1):
    if i % 5 == 0:
        continue
    print(i)