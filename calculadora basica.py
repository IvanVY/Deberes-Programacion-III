##Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.
num1 = float(input("Escriba el primer numero: "))
num2 = float(input("Escriba el segundo numero: "))
signo = input("Escriba la operacion que desea realizar +, -, *, /: ")
if(signo == "+"):
    result = num1 + num2
    print("La suma es ", result)
if(signo == "-"):
    result = num1 - num2
    print("La resta es ", result)
if(signo == "*"):
    result = num1 * num2
    print("La multiplicacion es ", result)
if(signo == "/"):
    result = num1 / num2
    print("La division es ", result)
