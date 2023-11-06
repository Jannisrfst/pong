import turtle

def start_pong_game():
    window = turtle.Screen()
    window.title("Pong")
    window.setup(width=800, height=600)
    window.bgcolor("black")
    window.tracer(0)
    custom_font = ("Verdana", 18, "normal")

    # Klassen Instanz erstellen
    class Paddle(turtle.Turtle):
        def __init__(self, x, y):
            super().__init__()
            self.speed(0)
            self.shape("square")
            self.shapesize(stretch_wid=6, stretch_len=1)
            self.penup()
            self.color("white")
            self.goto(x, y)

    class Ball(turtle.Turtle):
        def __init__(self):
            super().__init__()
            self.speed(0)
            self.shape("circle")
            self.penup()
            self.color("white")
            self.goto(0, 0)
            self.dx = 0.1
            self.dy = 0.1

    # Funktionen für die Paddel-Bewegung
    def paddle1_up():
        y = paddle1.ycor()
        y += 20
        paddle1.sety(y)

    def paddle1_down():
        y = paddle1.ycor()
        y -= 20
        paddle1.sety(y)

    def paddle2_up():
        y = paddle2.ycor()
        y += 20
        paddle2.sety(y)

    def paddle2_down():
        y = paddle2.ycor()
        y -= 20
        paddle2.sety(y)

    # Objekte erstellen
    paddle1 = Paddle(-350, 0)
    paddle2 = Paddle(350, 0)
    ball = Ball()

    score1 = 0
    score2 = 0

    scb = turtle.Turtle()
    scb.shape("square")
    scb.color("white")
    scb.penup()
    scb.hideturtle()
    scb.goto(0, 260)
    scb.write("Player 1: 0  Player 2: 0", align="center", font=custom_font)

    speed_level = 1

    # Funktion zur Erhöhung der Geschwindigkeit
    def increase_speed():
        nonlocal speed_level
        if speed_level < 10:
            speed_level += 1
            ball.dx *= 1.1
            ball.dy *= 1.1

    window.listen()
    window.onkeypress(paddle1_up, "w")
    window.onkeypress(paddle1_down, "s")
    window.onkeypress(paddle2_up, "Up")
    window.onkeypress(paddle2_down, "Down")

    # Game Loop
    while True:
        window.update()

        # Bewegung des Balls
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Reflektion am Window
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        # Reflektion Paddles
        if (ball.xcor() > paddle2.xcor() - 10 and ball.xcor() < paddle2.xcor() + 10) and \
                (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
            ball.setx(paddle2.xcor() - 10)
            ball.dx *= -1

        if (ball.xcor() < paddle1.xcor() + 10 and ball.xcor() > paddle1.xcor() - 10) and \
                (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
            ball.setx(paddle1.xcor() + 10)
            ball.dx *= -1

        # Spieler bekommt Punkt, Ball wird in die Mitte gesetzt
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            scb.clear()
            scb.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=custom_font)
            increase_speed()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            scb.clear()
            scb.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=custom_font)
            increase_speed()
