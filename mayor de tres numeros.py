##Solicita tres números y determina cuál es el mayor.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

if (num1 > num2 and num1 > num3):
    print("El numero mayor es: ", num1)
elif (num2 > num1 and num2 > num3):
    print("El numero mayor es: ", num2)
elif (num3 > num1 and num3 > num2):
    print("El numero mayor es: ", num3)
elif (num1 == num2 and num1 == num3):
    print("Los numeros son iguales: ", num1)
