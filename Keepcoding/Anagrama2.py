def Anagrama(p1,p2):
    lista = list (p2)
    
    pos1 = 0
    aunOk = True
    
    while pos1 < len (p1) and aunOk:
        pos2 = 0
        encontrado = False
        while pos2 < len(lista) and not encontrado:
            if cadena[pos1] == lista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1
                
        if encontrado:
            lista[pos2] = None
        else:
            aunOk: False
            
        pos1 = pos1 + 1
        
        return aunOk
    print aunOk
            
        