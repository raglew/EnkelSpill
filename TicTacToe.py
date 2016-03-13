#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------  Tic Tac Toe med 2 spillere

# -------------------  Authors: EmilZach, Arxcis, raglew


from turtle import *
import random

# Init turtle
t = Turtle()
s = Screen()

# Init turtle
t.speed(8)

# --- Finne window boundries --- different on each machine
win_w = s.window_width()
win_h = s.window_height()

# --- Sette grensene for koordinatsystemet
max_x = win_w/2
min_x = win_w/2 * (-1)
max_y = win_h/2
min_y = win_h/2 * (-1)


# 1. Tegne grid
def tegne_grid():

    # --- Tegner TicTacToe-streker med relative koordinater ---
    t.penup()
    t.setpos(min_x + (2/3*win_w), max_y - (1/10*win_h))
    t.setheading(270)
    t.pendown()
    t.forward(8/10*win_h)

    t.penup()
    t.setpos(max_x - (1/10*win_w), min_y + (1/3*win_h))
    t.setheading(180)
    t.pendown()
    t.forward(8/10*win_w)

    t.penup()
    t.setpos(min_x + (1/3*win_w), max_y - (1/10*win_h))
    t.setheading(270)
    t.pendown()
    t.forward(8/10*win_h)

    t.penup()
    t.setpos(min_x + (1/10*win_w), min_y + (2/3*win_h))
    t.setheading(0)
    t.pendown()
    t.forward(8/10*win_w)


def tegne_rutenummer():
    """ Her skal vi tilegne hver rute i spillet et tall.
         Slik at spilleren vet hvilken tast han/hun skal 
          bruke for å skrive et kryss eller sirkel i den 
           bestemte ruten.
    --------------------------------------- Jonas ----- """    
    # Først en liste med tall fra 1, 9
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    liste_counter = 0
    t.penup()
    for i in range(3):    
        for k in range(3):
            t.goto(min_x + (win_w*1/10) + (win_w*1/3*k),
                   max_y - (win_h*1/10) - (win_h*1/3*i))
            t.color("blue")
            t.write(liste[liste_counter], move=False, align="center",
                    font=("Arial", 6, "bold"))
            liste_counter += 1


def hvem_starter():
    """  Her bruker vi biblioteket random, og funksjonen
          random.randrange() til å generere et tilfeldig tall
           som enten er 1 eller 2, for å bestemme hvilken spiller 
            som starter. 
             random.randrange(1, 3) henter et tall i listen [1, 2]
              En liste fra 1 til 3, men ikke inkludert 3, der altså.        
    --------------------------------------------------- Jonas ---- """
    spiller = random.randrange(1, 3)
    if spiller == 1:
        print("Spiller 1 starter.")
    else:
        print("Spiller 2 starter.")
    return spiller


def hvem_sin_tur():
    """ Denne funksjonen skriver en tekst oppe i venstre 
         hjørnet av spillet, som viser hvem sin tur det er. 
          Håpet er at denne skal oppdatere seg selv, etterhvert 
           som spillet uvikler seg. Annenhver gang skal den skrive 
            Spiller 1 og annenhver spiller 2.                   
    -------------------------------------------------- Jonas ----  """
    t.ht()
    t.penup()
    t.color("red")
    t.goto(min_x + (win_w * 0.5/10), max_y - (win_h * 0.7/10))
    t.pendown()
    t.write("Spiller %d sin tur" % spiller, move=False, align="left",
            font=("Arial", 15, "bold"))


def plassere(x, y):
    print(x, y)                                                                             # debug data
    # må lage en funksjon som behandle spillerens klikk                                     raglew

# Init graphics and logics
tegne_grid()
tegne_rutenummer()
spiller = hvem_starter()

# Main game
hvem_sin_tur()

# 2. Spiller 1 plassere

s.onclick(plassere)

# 3. Veksler spillere

# 3. Spiller 2 plassere

# 4. Inn til en av spillene winner


s.mainloop()
