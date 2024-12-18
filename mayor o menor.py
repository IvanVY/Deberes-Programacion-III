##Mayor o menor, Esriba un programa que solicite un número y determine si es mayor o menor que 10.
numC = 10
num = int(input("Digite un numero: "))
if numC > num:
    print(num, "es menor a 10")
elif numC == num:
    print(num, "es igual a 10")
else:
    print(num, "es mayor a 10")
