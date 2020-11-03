
    angulo = 360/16
    lista = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    cadenagrados = []
    contar = 0   
    
    for caracter in range(len(lista)):
        caractermult = lista[contar]
        multgrados = caractermult * angulo
        cadenagrados.append(multgrados)
        contar +=1

#lista2 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
#contar2 = 0

#for item in cadenagrados and item in lista2:
    #comparacion.append(item)
 
#if len(comparacion) > 0:
  #print ('Ambas listas contienen estos elementos')
  #for item in comparacion: print ('%s' % item)
#else:
  #print ('No existe ningun elemento igual en las listas')
    

#for caracter in lista:
    #valorHexadecimal = hex(ord(caracter))
    #digito1 = valorHexadecimal[2]
    #angulo1 = digitos16.index(digito1) * angulo
    
    #digito2 = valorHexadecimal[3]
    #angulo2 = digitos16.index(digito2) * angulo
    
    #print(digito1, "-", angulo1)
    #print(digito2, "-", angulo2)
    
