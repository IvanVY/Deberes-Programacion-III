##Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. Escribe un programa que calcule el monto final.
compra = float(input("Ingrese el valor total de compra: "))
if (compra > 100):
    descuento = compra * 0.2
    PFinal = compra - descuento
    print("Obtuvo un descuento del 20% en su compra de",compra,"$", "el valor a pagar sera",PFinal,"$")
else:
    print("El valor a pagar es:", compra,"$") 
