import turtle

screen = turtle.Screen()
screen.bgcolor("black")

Stellie = turtle.Turtle()
Stellie.width(2)
Stellie.speed(0)  
Stellie.color("blue")

def Swannie_se_vierkant(t, length):
  for i in range(4):
    t.forward(length)
    t.left(90)

def Swannie_se_vierkant_2(t, num, angle, length, scale):
  for i in range(num):
    Swannie_se_vierkant(t, length)
    t.left(angle)
    length = scale * length

Stellie.penup()
Stellie.goto(-5, -53)
Stellie.pendown()
Swannie_se_vierkant_2(Stellie, 90, 10, 200, 0.97)
