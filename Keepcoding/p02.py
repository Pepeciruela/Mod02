nombre= input("¿Cómo te llamas?")
print("Hola, ", nombre)

stredad= input("¿Cuántos años tienes?")
stranno= input("¿Qué año es?")
strmes= input("¿En que mes estamos?")
strdia= input ("¿En que día estamos?")

edad=int(stredad)
anno=int(stranno)
mes= int(strmes)
dia= int(strdia)

if mes == 1:
    transcurridos= dia
elif mes == 2:
    transcurridos= dia + 31
elif mes == 3:
    transcurridos= dia + 31+ 28
elif mes == 4:
    transcurridos= dia + 31+ 28 + 31
elif mes == 5:
    transcurridos= dia + 31+ 28 + 31 +30
elif mes == 6:
    transcurridos= dia + 31+ 28 + 31 +30 +31
elif mes == 7:
    transcurridos= dia + 31+ 28 + 31 +30+31+30
elif mes == 8:
    transcurridos= dia + 31+ 28 + 31 +30+31+30+31
elif mes == 9:
    transcurridos= dia + 31+ 28 + 31 +30+31+30+31+31
elif mes == 10:
    transcurridos= dia + 31+ 28 + 31 +30+31+30+31+31+30
elif mes == 11:
    transcurridos= dia + 31+ 28 + 31 +30+31+30+31+31+30+31
else :
    transcurridos= dia + 31+ 28 + 31 +30+31+30+31+31+30+31+31
    
prob = transcurridos / 365 * 100


nacimiento = anno-edad

print (nombre, "naciste en", nacimiento, "con una probabilidad de", prob)
print (" o en", nacimiento -1, "con una probabilidad de", 100-prob)
 
    
    
    
    
    
