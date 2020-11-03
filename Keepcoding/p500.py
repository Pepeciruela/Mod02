n1 = input("Dime un número")
n2= input("Dime otro número")

numero1 = int(n1)
numero2 = int(n2)

divnumero1 = numero1/10
divnumero2 = numero2/10
suma =(divnumero1 + divnumero2)
resta = (divnumero1 - divnumero2)
multiplicacion = (divnumero1 * divnumero2)
division = (divnumero1 / divnumero2)
redondeosuma = (round(suma,2))
redondeoresta = (round(resta,2))
redondeomultiplicacion = (round(multiplicacion,2))
redondeodivision = (round(division,2))

imprimirsuma = print ("{0} + {1} = {2}".format(divnumero1, divnumero2, redondeosuma, redondeoresta, redondeomultiplicacion, redondeodivision))
imprimirresta = print ("{0} - {1} = {3}".format(divnumero1, divnumero2, redondeosuma, redondeoresta, redondeomultiplicacion, redondeodivision))
imprimirmultiplicacion = print ("{0} * {1} = {4}".format(divnumero1, divnumero2, redondeosuma, redondeoresta, redondeomultiplicacion, redondeodivision))
imprimirdivision = print ("{0} / {1} = {5}".format(divnumero1, divnumero2, redondeosuma, redondeoresta, redondeomultiplicacion, redondeodivision))
