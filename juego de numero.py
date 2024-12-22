##Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número. Usa if para verificar si acertó o no.

##importar modulo aleatorio
import random
## randint() el método devuelve un número entero número de elemento seleccionado del rango especificado.
##guardamos el numero aleatorio en numeroAleatorio
numeroAleatorio = random.randint(1,10)

num = int(input("Adivine un numero entre el 1 y 10: "))

if(numeroAleatorio == num):
    print("Ganaste, el numero correcto es: ", numeroAleatorio)
else:
    print("Perdiste, el numero correcto es: ", numeroAleatorio)
