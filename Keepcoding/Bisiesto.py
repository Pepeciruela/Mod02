strnumero = input("Introduce un año: ")
try:
    numero = int(strnumero)
except ValueError:
    print ("Debes introducir un número entero")
    strnumero = input ("Introduce un año: ")   
else:
    numero = int(strnumero)

def Bisiesto():
    if numero % 400 == 0:
        return True
    elif numero % 400 != 0:
        if numero % 100 == 0:
            return True
        if numero % 4 == 0:
            return True
    else:
        return True

if Bisiesto () == True:
    print ( "El año", numero, "es Bisiesto")
else:
    print ( "El año", numero, "no es Bisiesto")
        
   