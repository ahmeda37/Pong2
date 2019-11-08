import turtle
import winsound

def init_piece(ball):
    result = turtle.Turtle()
    result.speed(0)
    result.shape("square")
    if not ball:
        result.shapesize(stretch_wid=5, stretch_len=1)
    result.color("white")
    result.penup()
    return result

def init_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    return pen

def draw_score(pen, score1, score2):
    pen.clear()
    pen.write("Player A: {0} Player B: {1}".format(score1,score2), align="center", font=("Courier", 24, "normal"))


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
ball.dx = .5
ball.dy = .5

# Score
pen = init_score()


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

player_1 = 0
player_2 = 0

# GAME LOOP
while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1 += 1


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2 += 1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if paddle_1.ycor() > 340:
        paddle_1.sety(-340)

    if paddle_1.ycor() < -340:
        paddle_1.sety(340)

    if paddle_2.ycor() > 340:
        paddle_2.sety(-340)

    if paddle_2.ycor() < -340:
        paddle_2.sety(340)

    draw_score(pen, player_1, player_2)