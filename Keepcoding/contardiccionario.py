mitexto = "tres palabras para ti"

frecuencias = dict()

for caracter in mitexto:
    if caracter in frecuencias:
        frecuencias [caracter] +=1
    else:
        frecuencias [caracter] = 1
        
for letra in frecuencias.keys():
    print (letra, "-", frecuencias [letra])