#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tic Tac Toe med 2 spillere

import turtle as t
import random

t.screensize(500, 500)

# 1. Tegne grid

t.penup()
t.setpos(200, 200)
t.setheading(270)
t.pendown()
t.forward(500)

t.penup()
t.setpos(350, -125)
t.setheading(180)
t.pendown()
t.forward(500)

t.penup()
t.setpos(0, 200)
t.setheading(270)
t.pendown()
t.forward(500)

t.penup()
t.setpos(-150, 50)
t.setheading(0)
t.pendown()
t.forward(500)

# 2. Spiller 1 plassere
# 3. Spiller 2 plassere
# 4. Inn til en av spillene winner

# Disse funksjonene må være med for at programmet skal fungere.

t.listen()
t.mainloop()
