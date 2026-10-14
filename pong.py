"""
Egyszerű, kétjátékos Pong játék.
Csak a Python beépített turtle modulját használja.
"""

import turtle

# Ablak beállítása
ablak = turtle.Screen()
ablak.title("Python Pong")
ablak.bgcolor("black")
ablak.setup(width=800, height=600)
ablak.tracer(0)

# Pontszámok
bal_pont = 0
jobb_pont = 0

# Bal ütő
bal_uto = turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.color("white")
bal_uto.shapesize(stretch_wid=5, stretch_len=1)
bal_uto.penup()
bal_uto.goto(-350, 0)

# Jobb ütő
jobb_uto = turtle.Turtle()
jobb_uto.speed(0)
jobb_uto.shape("square")
jobb_uto.color("white")
jobb_uto.shapesize(stretch_wid=5, stretch_len=1)
jobb_uto.penup()
jobb_uto.goto(350, 0)

# Labda
labda = turtle.Turtle()
labda.speed(0)
labda.shape("circle")
labda.color("white")
labda.penup()
labda.goto(0, 0)
labda.dx = 0.12
labda.dy = 0.12

# Pontszám kijelzése
kiiras = turtle.Turtle()
kiiras.speed(0)
kiiras.color("white")
kiiras.penup()
kiiras.hideturtle()
kiiras.goto(0, 260)


def pontszam_frissit():
    """Kiírja az aktuális pontszámot."""
    kiiras.clear()
    kiiras.write(
        f"Bal: {bal_pont}    Jobb: {jobb_pont}",
        align="center",
        font=("Arial", 20, "normal"),
    )


def bal_fel():
    """A bal ütőt felfelé mozgatja."""
    y = bal_uto.ycor()
    if y < 250:
        bal_uto.sety(y + 20)


def bal_le():
    """A bal ütőt lefelé mozgatja."""
    y = bal_uto.ycor()
    if y > -240:
        bal_uto.sety(y - 20)


def jobb_fel():
    """A jobb ütőt felfelé mozgatja."""
    y = jobb_uto.ycor()
    if y < 250:
        jobb_uto.sety(y + 20)


def jobb_le():
    """A jobb ütőt lefelé mozgatja."""
    y = jobb_uto.ycor()
    if y > -240:
        jobb_uto.sety(y - 20)


# Billentyűk hozzárendelése
ablak.listen()
ablak.onkeypress(bal_fel, "w")
ablak.onkeypress(bal_le, "s")
ablak.onkeypress(jobb_fel, "Up")
ablak.onkeypress(jobb_le, "Down")

pontszam_frissit()

# Játékciklus
while True:
    ablak.update()

    # A labda mozgatása
    labda.setx(labda.xcor() + labda.dx)
    labda.sety(labda.ycor() + labda.dy)

    # Ütközés a felső és alsó fallal
    if labda.ycor() > 290:
        labda.sety(290)
        labda.dy *= -1

    if labda.ycor() < -290:
        labda.sety(-290)
        labda.dy *= -1

    # A labda elhagyta a pályát a jobb oldalon
    if labda.xcor() > 390:
        bal_pont += 1
        labda.goto(0, 0)
        labda.dx *= -1
        pontszam_frissit()

    # A labda elhagyta a pályát a bal oldalon
    if labda.xcor() < -390:
        jobb_pont += 1
        labda.goto(0, 0)
        labda.dx *= -1
        pontszam_frissit()

    # Ütközés a jobb ütővel
    if (
        330 < labda.xcor() < 350
        and jobb_uto.ycor() - 50 < labda.ycor() < jobb_uto.ycor() + 50
    ):
        labda.setx(330)
        labda.dx *= -1

    # Ütközés a bal ütővel
    if (
        -350 < labda.xcor() < -330
        and bal_uto.ycor() - 50 < labda.ycor() < bal_uto.ycor() + 50
    ):
        labda.setx(-330)
        labda.dx *= -1
