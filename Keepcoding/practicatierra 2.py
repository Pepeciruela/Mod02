angulos = [22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]
angulo = 360 /16

list = ("22.5", "45.0", "67.5", "90.0", "112.5", "135.0", "157.5", "180.0", "202.5", "225.0", "247.5", "270.0", "292.5", "315.0", "337.5")
new_list = []
for item in list:
    new_list.append(float(item))

contar = 0
lista_Hexa =[]

for caracter in range (len(new_list)):
    valorHexadecimal =  new_list [contar]
    digito1 = valorHexadecimal/(angulo)
    lista_Hexa.append(digito1)
    contar += 1

contar1 = 0
listaletra = []
for item in range (len(lista_Hexa)):
    if item > contar1 and item <= 9:
        listaletra.append(str(item))
        contar+=1
    if item == 9:
        listaletra.append("a")
    if item == 10:
        listaletra.append("b")
    if item == 11:
        listaletra.append("c")    
    if item == 12:
        listaletra.append("d")    
    if item == 13:
        listaletra.append("e")    
    if item == 14:
        listaletra.append("f")





    
    
   