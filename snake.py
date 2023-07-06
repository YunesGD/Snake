import turtle
import time
import random


window = turtle.Screen()
window.title('snake gmae')
window.bgpic('Desert.gif')
window.addshape('apple.gif')
window.addshape('apple-big.gif')
window.addshape('snake.gif')
window.addshape('mine.gif')
window.bgcolor('black')
window.setup(690, 785)
window.tracer(0)


assistant_base = turtle.Turtle()
assistant_base.color('red')
assistant_base.pensize(5)
assistant_base.penup()
assistant_base.hideturtle()
assistant_base.goto(-325, 325)
assistant_base.pendown()

for i in range(1, 5):
    assistant_base.forward(650)
    assistant_base.right(90)


assistant_base.color('orange')
assistant_base.penup()
assistant_base.goto(0, -375)
assistant_base.pendown()
assistant_base.write('Yunes Tooloe', align='center',
                     font=('caveat', 25, 'bold'))


assistant_base.penup()
assistant_base.pensize(0)
assistant_base.goto(-135, 345)
assistant_base.pendown()
for i in range(1, 3):
    assistant_base.forward(215)
    assistant_base.right(90)
    assistant_base.forward(5)
    assistant_base.right(90)

#                         score
Score = turtle.Turtle()
Score.color('orange')
Score.penup()
Score.hideturtle()
Score.goto(0, 355)
Score.write('Score :   0            High Score :  0 ',
            align='center', font=('caveat', 25, 'bold'))


#                         food
food = turtle.Turtle()
food.shape('apple.gif')
food.penup()
food.goto(-100, 100)

#                        big food
big_food = turtle.Turtle()
big_food.penup()
big_food.goto(400, 400)

#                        load bar
load_bar = turtle.Turtle()
load_bar.hideturtle()
load_bar.color('orange')
load_bar.penup()
load_bar.goto(100, 335)
load_bar.write('LVL :  1 ', font=('caveat', 15, 'bold'))
load_bar.goto(-135, 325)

mine = turtle.Turtle()
mine.shape('mine.gif')
mine.penup()
mine.goto(100, -100)

#                       snake = palyer
snake = turtle.Turtle()
snake.shape('snake.gif')
snake.penup()

snake.direction = 'Stop'


def go_up():
    if snake.direction != "Down":
        snake.direction = "Up"


def go_down():
    if snake.direction != "Up":
        snake.direction = "Down"


def go_right():
    if snake.direction != "Left":
        snake.direction = "Right"


def go_left():
    if snake.direction != "Right":
        snake.direction = "Left"


def move():
    if snake.direction == 'Up':
        y = snake.ycor()
        snake.sety(y+15)

    if snake.direction == 'Down':
        y = snake.ycor()
        snake.sety(y-15)

    if snake.direction == 'Right':
        x = snake.xcor()
        snake.setx(x+15)

    if snake.direction == 'Left':
        x = snake.xcor()
        snake.setx(x-15)


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")


score = 0
high_score = 0
counter_food = 0
counter_bar = 0
LVL = 1
delay = 0.1
Tails = []
mines = []
M = 0
mines.append(mine)

while True:
    window.update()
    time.sleep(delay)

    if snake.distance(food) < 23:
        #                               random food
        i = random.randint(-300, 290)
        j = random.randint(-300, 290)
        food.goto(i, j)
        food.shape('apple.gif')

        #                               random mine
        x = random.randint(-300, 290)
        y = random.randint(-300, 290)
        mines[M].goto(x, y)

        #                               sanke tail
        tail = turtle.Turtle()
        tail.shape('circle')
        tail.color('green')
        tail.penup()
        Tails.append(tail)

        load_bar.write('--', move=True, font=('caveat', 25, 'bold'))

        score += 10
        delay -= 0.001
        counter_food += 1
        counter_bar += 1

        if score > high_score:
            high_score = score
        Score.clear()
        Score.write('Score :   {}           High Score :  {} '.format(score, high_score), align='center',
                    font=('caveat', 25, 'bold'))

    if counter_bar == 10:
        counter_bar = 0
        load_bar.clear()
        load_bar.goto(100, 335)
        LVL += 1
        load_bar.write('LVL :  {}'.format(LVL),
                       font=('caveat', 15, 'bold'))
        load_bar.goto(-135, 325)

        mine = turtle.Turtle()
        mine.shape('mine.gif')
        mine.penup()
        mine.goto(100, -100)
        mines.append(mine)
        M += 1

    for i in mines:
        if i.distance(snake) < 23:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = 'stop'
            food.goto(-100, 100)
            mine.goto(100, -100)
            load_bar.clear()
            load_bar.goto(100, 335)
            load_bar.write('LVL :  1 ', font=('caveat', 15, 'bold'))
            load_bar.goto(-135, 325)
            counter_food = 0
            counter_bar = 0
            LVL = 1

    for index in range(len(Tails)-1, 0, -1):
        i = Tails[index-1].xcor()
        j = Tails[index-1].ycor()
        Tails[index].goto(i, j)

    if len(Tails) > 0:
        i = snake.xcor()
        j = snake.ycor()
        Tails[0].goto(i, j)
    move()

    if counter_food == 5:
        big_food.shape('apple-big.gif')
        i = random.randint(-300, 290)
        j = random.randint(-300, 290)
        big_food.goto(i, j)
        counter_food = 0

    if snake.distance(big_food) < 40:
        big_food.goto(800, 800)
        score += 50
        high_score = score
        Score.clear()
        Score.write('Score :   {}           High Score :  {} '.format(score, high_score), align='center',
                    font=('caveat', 25, 'bold'))
        load_bar.write('--', move=True, font=('caveat', 25, 'bold'))
        counter_bar += 1

    if -310 > snake.xcor() or snake.xcor() > 310 or snake.ycor() > 280 or snake.ycor() < -330:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = 'stop'
        food.goto(-100, 100)
        mine.goto(100, -100)
        load_bar.clear()
        load_bar.goto(100, 335)
        load_bar.write('LVL :  1 ', font=('caveat', 15, 'bold'))
        load_bar.goto(-135, 325)
        counter_bar = 0
        LVL = 1

        for i in Tails:
            i.goto(800, 800)
        Tails.clear()
        for i in mines:
            i.goto(800, 800)
        Tails.clear()

        delay = 0.1
        counter_food = 0
        score = 0
        Score.clear()
        Score.write('Score :   {}           High Score :  {} '.format(score, high_score), align='center',
                    font=('caveat', 25, 'bold'))

    for i in Tails:
        if i.distance(snake) < 15:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = 'stop'
            food.goto(-100, 100)
            mine.goto(100, -100)
            load_bar.clear()
            load_bar.goto(100, 335)
            load_bar.write('LVL :  1 ', font=('caveat', 15, 'bold'))
            load_bar.goto(-135, 325)
            counter_food = 0
            counter_bar = 0
            LVL = 1

            for i in Tails:
                i.goto(800, 800)
            Tails.clear()

            score = 0
            delay = 0.1
            Score.clear()
            Score.write('Score :   {}           High Score :  {} '.format(score, high_score), align='center',
                        font=('caveat', 25, 'bold'))


turtle.mainloop()
