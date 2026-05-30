import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

clock = turtle.Turtle()
clock.hideturtle()
clock.color("white")
clock.penup()

while True:
    current_time = time.strftime("%H:%M:%S")

    clock.clear()
    clock.write(
        current_time,
        align="center",
        font=("Arial", 40, "bold")
    )

    time.sleep(1)