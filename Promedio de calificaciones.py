##o	Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.
calificacion = 0
i = int(1)
suma = 0
while (calificacion >= 0):
    calificacion = int(input("Ingrese su calificacion de 1 al 10, o escriba -1 para terminar: "))
    if (calificacion >= 0):
        suma = calificacion + suma
        promedio = suma / i
        i += 1     
print("Su promedio es: ",promedio)
