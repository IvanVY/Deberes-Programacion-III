##Solicita la edad del usuario y determina si es elegible para votar (mayor o igual a 18 años).
edad = int(input("Ingrese su edad: "))
if (edad >= 18):
    print("Puede votar")
else:
    print("No puede votar")
