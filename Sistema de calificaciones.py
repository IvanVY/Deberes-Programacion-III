##Solicita una calificación numérica y devuelve la letra correspondiente:
calificacion = float(input("Ingrese la calificacion: "))
if (calificacion >= 90 and calificacion <=100):
    print("Obtuvo una A")
elif (calificacion >= 80 and calificacion <=89):
    print("Obtuvo una B")
elif (calificacion >= 70 and calificacion <= 79):
    print("Obtuvo una C")
elif (calificacion >= 60 and calificacion <= 69):
    print("Obtuvo una D")
elif (calificacion < 60):
    print("Obtuvo una F")
else:
    print("Calificacion no reconocida")
