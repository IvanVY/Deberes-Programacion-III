##Solicita un año y determina si es bisiesto (divisible entre 4 pero no entre 100, excepto si es divisible entre 400).
anio = int(input("Escriba un año: "))
if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
