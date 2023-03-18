# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

axiom = 'F-G-G'
rules = {'F' : 'F-G+F+G-F', 'G' : 'GG'} 
for i in range(6):
    aux = ''
    for char in axiom:
        if char in rules:
            aux += rules[char]
        else:
            aux += char
    axiom = aux

turtle.tracer(False)
turtle.speed('fastest')
turtle.color('#2B853B')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-300, -200)  
turtle.pensize(2)
turtle.pendown()
for char in axiom:
    if char == 'F' or char == 'G':
        turtle.forward(9)
    elif char == '-':
        turtle.left(120)
    elif char == '+':
        turtle.right(120)
    
turtle.exitonclick()
turtle.tracer(True)