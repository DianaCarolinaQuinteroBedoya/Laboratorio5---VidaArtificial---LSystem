# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

axiom = 'FX'
rules = {'X' : 'X+YF', 'Y' : 'FX-Y'} 
for i in range(10):
    aux = ''
    for char in axiom:
        if char in rules:
            aux += rules[char]
        else:
            aux += char
    axiom = aux

turtle.tracer(False)
turtle.color('#673000')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-100, 0)  
turtle.pensize(2)
turtle.pendown()
turtle.left(90)

for char in axiom:
    if char == 'F':
        turtle.forward(10)
    elif char == '-':
        turtle.left(90)
    elif char == '+':
        turtle.right(90)
    
turtle.exitonclick()
turtle.tracer(True)