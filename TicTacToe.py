#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tic Tac Toe med 2 spillere

from turtle import *
import random

# Init turtle
t = Turtle()
s = Screen()


# 1. Tegne grid
def tegne_grid():

    # --- Finne window boundries --- different on each machine
    win_width = s.window_width()
    win_height = s.window_height()

    # --- Sette grensene for koordinatsystemet
    max_x = win_width/2
    min_x = win_width/2 * (-1)
    max_y = win_height/2
    min_y = win_height/2 * (-1)

    # --- Tegner TicTacToe-streker med relative koordinater ---
    t.penup()
    t.setpos(min_x + (2/3*win_width), max_y - (1/10*win_height))
    t.setheading(270)
    t.pendown()
    t.forward(8/10*win_height)

    t.penup()
    t.setpos(max_x - (1/10*win_width), min_y + (1/3*win_height))
    t.setheading(180)
    t.pendown()
    t.forward(8/10*win_width)

    t.penup()
    t.setpos(min_x + (1/3*win_width), max_y - (1/10*win_height))
    t.setheading(270)
    t.pendown()
    t.forward(8/10*win_height)

    t.penup()
    t.setpos(min_x + (1/10*win_width), min_y + (2/3*win_height))
    t.setheading(0)
    t.pendown()
    t.forward(8/10*win_width)

# Spiller-logikken

spiller = random.randrange(1, 2)

if spiller == 1:
    print("Spiller 1 starter.")
else:
    print("Spiller 2 starter.")

# random.randrange(a,b) og random.randint(a,b) gir alltid resultatet 1 til variabel "spiller". Hvorfor den gjør det er usikkert. 

"""
Under denne kommentaren tenker jeg vi kunne lage en liste der vi setter X og Y koordinatene til senter av kvadratene.
Grunnet for dette er for la brukeren skrive ned hvilke kvadrat som skal bli merket med enten kryss eller sirkel slik at den kvadraten er tatt.

Jeg har tatt med strings med tall i for å kunne gjenkjenne hvilken kvadrat det er og hvilke X og Y koordinater den har.

- Emil
"""
kvadrat = ["" [x, y]]

kvadrat["1"]
kvadrat["2"]
kvadrat["3"]
kvadrat["4"]
kvadrat["5"]
kvadrat["6"]
kvadrat["7"]
kvadrat["8"]
kvadrat["9"]



# Avgjør hvem som vinner eller om det er tie



# Disse funksjonene må være med for at programmet skal fungere.

t.listen()
t.mainloop()