#Irina Kaminsky Castillo
#Axel Uzeta Gómez
#Edgar Zúñiga Sánchez
#Regina Vega Francia

from turtle import *
from random import randrange
from freegames import square, vector

food = [vector(0, 0)]
snake = [vector(10, 0)]
aim = vector(0, -10)

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def movefood():
    "Move snake forward one segment."
    foodhead = food[-1].copy()
    foodhead.move(aim)

    if not inside(foodhead) or foodhead in food:
        square(head.x, head.y, 9, 'red')
        update()
        return

    food.append(foodhead)
    
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
# 
#      if head == foodhead:
#         print('Snake:', len(snake))
#         food.x = randrange(-15, 15) * 10
#         food.y = randrange(-15, 15) * 10
#     else:
#         snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
        
    for body in food:
        square(bodyf.x, bodyf.y, 9, 'green')

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
movefood()
move()
done()
