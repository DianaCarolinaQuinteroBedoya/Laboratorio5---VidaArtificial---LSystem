# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

axiom = 'F-F-F-F'
rules = {'F' : 'F-F+F+FF-F-F+F'}
for i in range(4):
    aux = ''
    for char in axiom:
        if char in rules:
            aux += rules[char]
        else:
            aux += char
    axiom = aux

turtle.tracer(False)
turtle.color('#2B853B')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-100, -100)  
turtle.pensize(1)
turtle.pendown()
for char in axiom:
    if char == 'F':
        turtle.forward(1)
    elif char == '-':
        turtle.left(90)
    elif char == '+':
        turtle.right(90)
    
turtle.exitonclick()
turtle.tracer(True)