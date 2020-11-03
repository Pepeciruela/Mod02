def esnumero(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
strunidades = input ("Introduce las unidades")    
while not esnumero(strunidades):
    print(esnumero, "debe ser un numero")
    strunidades = input ("Introduce las unidades")

strprecio = input ("Introduce el precio")
while not esnumero(strprecio):
    print(esnumero, "debe ser un numero")
    strprecio = input ("Introduce el precio")

unidades = float (strunidades)
precio = float (strprecio)

totalunidades = 0
totalprecio = 0

while unidades > 0:
    totalunidades = totalunidades + unidades
    strunidades = input ("Introduce las unidades")    
    while not esnumero(strunidades):
        print(esnumero, "debe ser un numero")
        strunidades = input ("Introduce las unidades")

while precio > 0:
    totalprecio = totalprecio + precio
    strprecio = input ("Introduce el precio")
    while not esnumero(strprecio):
        print(esnumero, "debe ser un numero")
        strprecio = input ("Introduce el precio")   
else:
    print ("unidades", totalunidades)

    

