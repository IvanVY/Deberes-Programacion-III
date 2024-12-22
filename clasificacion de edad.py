##Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).
edad = int(input("Ingrese su edad: "))
if (edad >= 0 and edad <= 12):
    print("Eres un/a niño/a")
elif (edad >= 13 and edad <= 17):
    print("Eres adolescente")
elif (edad >= 18):
    print("Eres adulto")
else:
    print("Edad no valida")
