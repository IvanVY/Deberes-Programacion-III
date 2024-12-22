##o	Solicita un número entero y muestra su versión invertida.
num = int(input("Ingrese un número entero: "))
invertido = 0

n = abs(num)  # Tomamos el valor absoluto para manejar números negativos

# Proceso de inversión de los dígitos
while (n > 0):
    #Obtener el último dígito de 'n' y agregarlo al número invertido
    #El operador n % 10 da el resto de la división de n entre 10, lo que equivale al último dígito del número.
    #desplaza los dígitos ya existentes en invertido una posición hacia la izquierda
    invertido = invertido * 10 + (n % 10)
    # Eliminar el último dígito de 'n'
    n = n // 10

# Si el número original era negativo, ajustamos el signo
if num < 0:
    invertido = -invertido

# Mostrar el número invertido
print("El número invertido es:", invertido)
