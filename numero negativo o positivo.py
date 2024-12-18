##Solicita al usuario un número y determina si es positivo, negativo o cero.

num = int(input("Digite un numero; "))

if num == 0:
    print(num, "es 0")
elif num > 0:
    print(num, "es un numero positivo")
else:
    print(num, "es un numero negativo")
