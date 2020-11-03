p1 = list ("mora")
p2 = list ("roma")

comparacion1 = []
comparacion2 = []

pos = 0
coincide = True

for caracter in p1:
    if caracter in p2:
        comparacion1.append (caracter)
        
for caracter in p2:
    if caracter in p1:
        comparacion2.append (caracter)



    
    