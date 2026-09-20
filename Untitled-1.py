import turtle

import turtle


window = turtle.Screen()
window.bgcolor("red")

pen = turtle.Turtle()
pen.speed(10)
pen.color("white")
pen.penup()
pen.goto(-100, 50)
pen.pendown()

# Fixed syntax, quotes, and font parameter tuple structure
pen.write("Jai Shree Ram", font=("Arial", 5, "bold"))

pen.hideturtle()  # Hides the turtle cursor for a cleaner look
window.mainloop()
