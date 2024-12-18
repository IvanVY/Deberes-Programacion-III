##Solicita un nombre de usuario y contraseña, y valida si ambos son correctos. Permite tres intentos antes de bloquear el acceso.
contraseniaP = "123"
usuarioP = "admin"
intentos = int(0)

while(intentos < 3):
    usuario = str(input("Ingrese su nombre de usuario: "))
    contrasenia = str(input("Ingrese su contraseña: "))
    if (usuarioP == usuario and contraseniaP == contrasenia):
        print("Bienvenido",usuarioP)
        break
    else:
        print("Contraseña incorrecta")
    intentos = intentos + 1
    if (intentos == 3):
        print("Intento muchas veces, regrese en 20 minutos")

