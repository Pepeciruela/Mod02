datos = input ("¿Qué tipo de grados quieres convertir? Introduce F o C: ")
salida = str(datos)

celsius = list(range (0,101))
fahrenheit = list(range (0,231))

while salida.lower() not in {"c", "C", "f", "F"}:
    print("Debes introducir F o C")
    datos = input ("¿Qué tipo de grados quieres convertir? Introduce F o C")
    salida = str(datos) 
    
else:
    while salida.lower() in {"c", "C"}:
        centigrados = input ("Introduce los grados: ")
        c = float (centigrados)
        
        while c not in celsius:
                print("Debes introducir un número entre 0 y 100")
                centigrados = input ("Introduce los grados: ")
                c = float (centigrados)    
        
        while c in celsius:
            c1 = c * 9/5 + 32
            print (c, "grados celsius equivalen a", round(c1,2), "grados fahrenheit")
            quit()
            
    while salida.lower() in {"f", "F"}:
        faren = input ("Introduce los grados: ")
        f = float (faren)
        
        while f not in fahrenheit:
                print("Debes introducir un número entre 0 y 230")
                faren = input ("Introduce los grados: ")
                f = float (faren)    
        
        while f in fahrenheit:
            f1 = (f - 32) * 5/9
            print (f, "grados fahrenheit equivalen a", round(f1,2), "grados celsius")
            quit ()