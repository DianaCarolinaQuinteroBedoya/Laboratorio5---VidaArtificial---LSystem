# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

axiom = 'F'
rules = {'F' : 'F[+F[+F]-F][-F]F'} 
for i in range(5):
    aux = ''
    for char in axiom:
        if char in rules:
            aux += rules[char]
        else:
            aux += char
    axiom = aux

stack = []

turtle.tracer(False)
turtle.speed('fastest')
turtle.color('#2B853B')
turtle.speed('fastest')
turtle.penup()
turtle.goto(0, -300)  
turtle.pensize(1)
turtle.pendown()
turtle.left(90)

def push_state():
    x = turtle.xcor()
    y = turtle.ycor()
    heading = turtle.heading()
    stack.append((x, y, heading))

def pop_state():
    x, y, heading = stack.pop()
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.down()

for char in axiom:
    if char == 'F':
        turtle.forward(10)
    elif char == '-':
        turtle.left(21)
    elif char == '+':
        turtle.right(21)
    elif char == '[':
        push_state()
    elif char == ']':
        pop_state()

turtle.exitonclick()
turtle.tracer(True)