import turtle
import random
def draw_circle():
    r = random.randint(10, 80)
    turtle.circle(r)
def draw_square():
    size = random.randint(20, 100)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
def draw_triangle():
    size = random.randint(30, 100)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
turtle.speed(0)          
turtle.bgcolor("black")  
turtle.color("lime")     
n = int(input("скільки фігур намалювати? "))
for _ in range(n):
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(random.choice(["red", "yellow", "cyan", "lime", "orange", "white", "violet"]))
    shape = random.choice(["circle", "square", "triangle"])
    if shape == "circle":
        draw_circle()
    elif shape == "square":
        draw_square()
    else:
        draw_triangle()
turtle.hideturtle()
turtle.done()
