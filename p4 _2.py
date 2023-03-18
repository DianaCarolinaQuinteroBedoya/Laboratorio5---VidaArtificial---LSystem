# Diana Carolina Quintero Bedoya
# Juan Diego Varón Guarín
# Laboratorio 5: Sistemas-L

import turtle

import random
axiom1 = 'F'
axiom2 = 'F'
axiom3 = 'F'
axiom4 = 'F'
axiom5 = 'F'
axiom6 = 'F'
axiom7 = 'F'
axiom8 = 'F'
axiom9 = 'G'
axiom10 = 'G'

rules1 = ['F[+F]F[-F]F', 'F[-F]F[+F]F', 'F[-FF-F]F']
rules2 = {'F' : 'F[+F]F[-F[+F][-F]]F'}
rules3 = {'F' : 'F[+F[+F]-F][-F]F'}
rules4 = {'F' : 'FF+[+F-F-F]-[-F+F+F]'} 
rules5 = {'F' : 'FF', 'G' : 'FG[-F[G]-G][G+G][+F[G]+G]'} 

def code(axiom, rules):
    for i in range(5):
        aux = ''
        for char in axiom:
            if char == 'F':
                aux += rules[int(random.uniform(0,3))]
            else:
                aux += char
        axiom = aux
    return axiom

def code1(axiom, rules):
    for i in range(5):
        aux = ''
        for char in axiom:
            if char in rules:
                aux += rules[char]
            else:
                aux += char
        axiom = aux
    return axiom

axiom1 = code(axiom1, rules1)
axiom2 = code(axiom2, rules1)
axiom3 = code(axiom3, rules1)
axiom4 = code1(axiom4, rules2)
axiom5 = code1(axiom5, rules3)
axiom6 = code1(axiom6, rules4)
axiom7 = code1(axiom7, rules2)
axiom8 = code1(axiom8, rules3)
axiom9 = code1(axiom9, rules5)
axiom10 = code1(axiom10, rules5)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
turtle5 = turtle.Turtle()
turtle6 = turtle.Turtle()
turtle7 = turtle.Turtle()
turtle8 = turtle.Turtle()
turtle9 = turtle.Turtle()
turtle10 = turtle.Turtle()

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []
stack10 = []

turtle.tracer(False)
turtle.colormode(255)
turtle1.speed('fastest')
turtle1.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle1.penup()
turtle1.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle1.pensize(1)
turtle1.pendown()
turtle1.left(90)

turtle2.speed('fastest')
turtle2.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle2.penup()
turtle2.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle2.pensize(1)
turtle2.pendown()
turtle2.left(90)

turtle3.speed('fastest')
turtle3.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle3.penup()
turtle3.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle3.pensize(1)
turtle3.pendown()
turtle3.left(90)

turtle4.speed('fastest')
turtle4.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle4.penup()
turtle4.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle4.pensize(1)
turtle4.pendown()
turtle4.left(90)

turtle5.speed('fastest')
turtle5.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle5.penup()
turtle5.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle5.pensize(1)
turtle5.pendown()
turtle5.left(90)

turtle6.speed('fastest')
turtle6.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle6.penup()
turtle6.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle6.pensize(1)
turtle6.pendown()
turtle6.left(90)

turtle7.speed('fastest')
turtle7.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle7.penup()
turtle7.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle7.pensize(1)
turtle7.pendown()
turtle7.left(90)

turtle8.speed('fastest')
turtle8.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle8.penup()
turtle8.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle8.pensize(1)
turtle8.pendown()
turtle8.left(90)

turtle9.speed('fastest')
turtle9.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle9.penup()
turtle9.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle9.pensize(1)
turtle9.pendown()
turtle9.left(90)

turtle10.speed('fastest')
turtle10.color(int(random.uniform(0, 255)),int(random.uniform(0, 255)),int(random.uniform(0, 255)))
turtle10.penup()
turtle10.goto(int(random.uniform(-450, 450)), int(random.uniform(-450, 0)))  
turtle10.pensize(1)
turtle10.pendown()
turtle10.left(90)

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

def draw(stack, turtle, axiom, size):
    for char in axiom:
        if char == 'F' or char == 'G':
            turtle.forward(size)
        elif char == '-':
            turtle.left(22.5)
        elif char == '+':
            turtle.right(22.5)
        elif char == '[':
            push_state(stack, turtle)
        elif char == ']':
            pop_state(stack, turtle)

draw(stack1, turtle1, axiom1, int(random.uniform(2,6)))
draw(stack2, turtle2, axiom2, int(random.uniform(2,6)))
draw(stack3, turtle3, axiom3, int(random.uniform(2,6)))
draw(stack4, turtle4, axiom4, int(random.uniform(2,6)))
draw(stack5, turtle5, axiom5, int(random.uniform(2,6)))
draw(stack6, turtle6, axiom6, int(random.uniform(2,6)))
draw(stack7, turtle7, axiom7, int(random.uniform(2,6)))
draw(stack8, turtle8, axiom8, int(random.uniform(2,6)))
draw(stack9, turtle9, axiom9, int(random.uniform(2,6)))
draw(stack10, turtle10, axiom10, int(random.uniform(2,6)))

turtle.exitonclick()
turtle.tracer(True)