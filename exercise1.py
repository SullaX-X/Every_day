# Задача 8
# import turtle as t
# color_lst = ['red', 'blue', 'yellow', 'green', 'darkviolet', 'orange']
# for i in range(45):
#   t.pensize(i / 1.5)
#   t.color(color_lst[i % 6])
#   t.forward(i * 3)
#   t.left(45)
# t.Screen().mainloop()

# Задача 9
# import turtle as tu
# for _ in range(3):
#     tu.forward(100)
#     tu.left(120)
# tu.penup()
# tu.goto(0, 50)
# tu.pendown()
# for _ in range(3):
#     tu.forward(100)
#     tu.right(120)
# tu.Screen().mainloop()

# Задача 10
# import turtle as tu
# tu.hideturtle()
# tu.speed(-1)
# tu.pencolor('green')
# for i in range(-200, 200, 40):
#     tu.goto(i, -200)
#     tu.dot(10, 'blue')
#     tu.goto(0, 0)
# tu.dot(10, 'red')
# tu.Screen().mainloop()

# Задача 11
# import turtle as tu
# tu.speed(-1)
# tu.pensize(8)
# color_up = ['red', 'black', 'cyan']
# color_down = ['green', 'yellow']
# tu.pencolor('green')
# tu.circle(60)
# tu.penup()
# tu.pencolor('red')
# tu.goto(65, 60)
# tu.pendown()
# tu.circle(60)
# tu.penup()
# tu.pencolor('black')
# tu.goto(-60, 60)
# tu.pendown()
# tu.circle(60)
# tu.penup()
# tu.pencolor('cyan')
# tu.goto(-185, 60)
# tu.pendown()
# tu.circle(60)
# tu.penup()
# tu.pencolor('yellow')
# tu.goto(-125, 0)
# tu.pendown()
# tu.circle(60)
# tu.Screen().mainloop()

# Задача 12
# import turtle as tu
# tu.hideturtle()
# tu.speed(-1)
# # head
# tu.circle(80)
# tu.circle(40)
# # left
# tu.penup()
# tu.goto(80, 124)
# tu.pendown()
# tu.fillcolor('red')
# tu.begin_fill()
# tu.circle(30)
# tu.end_fill()
# # right
# tu.penup()
# tu.goto(-80, 124)
# tu.pendown()
# tu.circle(30)
# # eye left
# tu.penup()
# tu.goto(40, 84)
# tu.pendown()
# tu.dot(20)
# tu.dot(10, 'red')
# # eye right
# tu.penup()
# tu.goto(-40, 84)
# tu.pendown()
# tu.dot(20)
# tu.dot(10, 'red')
# # nose
# tu.penup()
# tu.goto(0, 50)
# tu.pendown()
# tu.dot(14)
# tu.pensize(2)
# tu.goto(0, 20)
# tu.Screen().mainloop()






















# Задача JUST
# from turtle import *
# from random import *
# colormode(255)
# bgcolor('black')
# hideturtle()
# penup()
# for i in range(500):
#     tracer(100)
#     fillcolor(randrange(255), randrange(255), randrange(255))
#     goto(randrange(-300, 300), randrange(-300, 300))
#     left(randrange(180))
#     begin_fill()
#     size_line = randrange(10, 40)
#     for _ in range(5):
#         right(144)
#         forward(size_line)
#     end_fill()
# mainloop()
