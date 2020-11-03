import screen

screen.locate(1,1)

dibujo1 = "**********"
dibujo2 = "*"

screen.locate (10,10)
print(dibujo1)

contador = 0
line = 11
column1 = 10
column2 = 20
if contador <= 10:
    screen.locate (line,column1)
    print(dibujo2)
    screen.locate (line,column2)
    print(dibujo2)
    contador += 1
    line += 1
    
screen.locate (21,10)
print(dibujo1)