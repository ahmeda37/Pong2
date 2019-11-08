import turtle


def init_piece(ball):
    result = turtle.Turtle()
    result.speed(0)
    result.shape("square")
    if not ball:
        result.shapesize(stretch_wid=5, stretch_len=1)
    result.color("white")
    result.penup()
    return result


# Init Turtle Module/ Setup Canvas
window = turtle.Screen()
window.title = "Pong by Abdurahman"
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle 1
paddle_1 = init_piece(False)
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = init_piece(False)
paddle_2.goto(350, 0)

# Ball
ball = init_piece(True)
ball.goto(0, 0)


def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard Binding
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# GAME LOOP
while True:
    window.update()

