# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

import random
axiom1 = 'F'
axiom2 = 'F'
axiom3 = 'F'

rules = ['F[+F]F[-F]F', 'F[-F]F[+F]F', 'F[-FF-F]F']

def code(axiom):
    for i in range(5):
        aux = ''
        for char in axiom:
            if char == 'F':
                aux += rules[int(random.uniform(0,3))]
            else:
                aux += char
        axiom = aux
    return axiom

axiom1 = code(axiom1)
axiom2 = code(axiom2)
axiom3 = code(axiom3)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

stack1 = []
stack2 = []
stack3 = []

turtle.tracer(False)
turtle1.speed('fastest')
turtle1.color('#2B853B')
turtle1.penup()
turtle1.goto(-300, -400)  
turtle1.pensize(1)
turtle1.pendown()
turtle1.left(90)

turtle2.speed('fastest')
turtle2.color('#2B853B')
turtle2.penup()
turtle2.goto(0, -400)  
turtle2.pensize(1)
turtle2.pendown()
turtle2.left(90)

turtle3.speed('fastest')
turtle3.color('#2B853B')
turtle3.penup()
turtle3.goto(300, -400)  
turtle3.pensize(1)
turtle3.pendown()
turtle3.left(90)

def push_state(stack, turtle):
    x = turtle.xcor()
    y = turtle.ycor()
    heading = turtle.heading()
    stack.append((x, y, heading))

def pop_state(stack, turtle):
    x, y, heading = stack.pop()
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.down()

def draw(stack, turtle, axiom):
    for char in axiom:
        if char == 'F' or char == 'G':
            turtle.forward(4)
        elif char == '-':
            turtle.left(22.5)
        elif char == '+':
            turtle.right(22.5)
        elif char == '[':
            push_state(stack, turtle)
        elif char == ']':
            pop_state(stack, turtle)

draw(stack1, turtle1, axiom1)
draw(stack2, turtle2, axiom2)
draw(stack3, turtle3, axiom3)

turtle.exitonclick()
turtle.tracer(True)