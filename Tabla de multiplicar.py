##Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
num = int(input("Ingrese el numero que desa la tabla de multiplicar: "))
i = int(1)
while(i <= 10):
    mult = num * i
    print(num, "x", i, "=", mult)
    i+=1
