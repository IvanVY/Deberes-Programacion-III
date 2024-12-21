## o	Calcula el factorial de un número ingresado por el usuario (n!).
factorial = int(1)
num = int(input("Ingrese el numero para factorial: "))
while (num > 1):
    factorial = num * factorial
    num -= 1
print(factorial)
