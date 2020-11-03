precio1 = 0
precio2 = 14
precio3 = 23
precio4 = 18

stredad = input ("Introduce la edad del cliente: ")

try:
   edad = int(stredad)
except ValueError:
    print ("Debes introducir un número entero")
    stredad = input ("Introduce la edad del cliente: ")   
else:
    edad = int(stredad)
    
listaedades =[]

while edad > 0:
    listaedades.append(edad)
    stredad = input ("Introduce la edad del cliente: ")
    edad = int(stredad)
if edad == 0:
    True

    listaprecios = []
    contar = 0
    
    
    for caracter in listaedades:
        precio = listaedades[contar]
        if precio <= 2:
            euros = precio1
        if 3 <= precio <=12:
            euros = precio2
        if 13 <= precio <=64:
            euros = precio3
        if 65 <= precio:
            euros = precio4
        if precio == 0:
            pass
        contar +=1
        listaprecios.append(euros)
    

contar1 = 0
sumababy = 0
preciobaby = 0
sumamenores = 0
preciomenores = 0
sumanormal = 0
precionormal = 0
sumajubilado = 0
preciojubilado = 0

for item in range(len(listaprecios)):
    item = listaprecios[contar1]
    if item == 0:
        sumababy += 1
        preciobaby += precio1
    if item == 14:
        sumamenores += 1
        preciomenores +=precio2
    if item == 23:
        sumanormal += 1
        precionormal += precio3
    if item == 18:
        sumajubilado += 1
        preciojubilado += precio4
    contar1 += 1

print (sumababy, "entradas de baby a 0 €:          ", preciobaby, "€" )
print (sumamenores, "entradas de menor a 14 €:       ", preciomenores, "€" )
print (sumanormal, "entradas normales a 23 €:       ", precionormal, "€" )
print (sumajubilado, "entradas de jubilado a 18 €:    ", preciojubilado, "€" )
print ("                                --------")
print ("                                 ", sum(listaprecios), "€")                          