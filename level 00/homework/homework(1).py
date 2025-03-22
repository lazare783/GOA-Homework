from turtle import * 
#we want to paint house
#step 1:   draw a square

speed(20)
color("green")
begin_fill()
width(7)
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
# drawing roof
penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(135)
forward(140)
left(90)
forward(140)
end_fill()

#drawing windows
penup()
goto(180,180)
pendown()

color("blue")
begin_fill()
left(45)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(20,140)
pendown()

color("blue")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


exitonclick()
