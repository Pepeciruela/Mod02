datos = input ("¿Qué tipo de grados quieres convertir? Introduce F o C")
salida = str(datos)

while salida == "C":
    gradosA = input ("Introduce el número de grados entre 0 y 100")
    grados1 = float(gradosA)
    while grados1> 0 <= 100:
        transformar = (grados1 * 9/5) +32
        print (grados1, "centigrados son", transformar, "grados fahrenheit")
        
    else:
        print (grados1, "debe ser un número entre 0 y 100")
        grados1 = input ("Introduce el número de grados entre 0 y 100")
            
if salida == "F":
    gradosB = input ("Introduce el número de grados entre 0 y 230")
    grados2 = float(gradosB)
    while grados2 > 0 <= 230:
        transformar = (grados2 - 32) * 5/9
        print (grados2, "fahrenheit son", transformar, "grados celsius")
    else:
        print (grados2, "debe ser un número entre 0 y 230")
        grados2 = input ("Introduce el número de grados entre 0 y 230")

else:
    print(salida, "debes introducir F o C")
    datos = input ("¿Qué tipo de grados quieres convertir? Introduce F o C")
    salida = str(datos)            
