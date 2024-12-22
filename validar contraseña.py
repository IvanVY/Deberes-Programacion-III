##Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345).
contrasenaF = int(12345)
contrasena = int(input("Ingrese su contraseña: "))
if (contrasenaF == contrasena):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
