##o	Solicita un número entero y calcula la suma de sus dígitos.
num = int(input("Ingrese un numero: "))
suma = 0
while (num > 0):
    
    # Obtener el último dígito de 'n' y sumarlo a 'suma'
    suma = suma + (num %10)
    
    # Eliminar el último dígito de 'n' usando división entera
    num = num//10
print("La suma de los digitos es: ",suma)
