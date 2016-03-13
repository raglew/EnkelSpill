"""

    Tittel: TicTacToe_ForslagJonas.py
    Opprettet: 16:52 - 11.03.2016
    Author: Jonas J. Solsvik
    Beskrivelse: Dette er en tekstfil, hvor jeg tester ut endringsforslag til 
                  Jeg kommer til å merge sammen med hovedfil, når jeg føler at 
                   det passe seg. No worries.
    ------------------------------------------------ Takk, Jonas ------------- """

from turtle import *    # --- endret Jonas
import random

# Init turtle
t = Turtle()
f = Turtle()
s = Screen()
i = Turtle()

# Init turtle
t.speed(8)
t.ht()

# -------------------init figur turtle  ------------  raglew
f.ht()
f.speed(0)
f.shape('circle')                               # sirkel som test
farge = 'red'                                   # variabel som kan brukes i svitsj_spiller funksjon
f.color(farge)                                 # rød farge som test
f.turtlesize(3)
f.penup()

# -------------------init instruks turtle ------------raglew
i.ht()
i.speed(0)
i.penup()

# --- Finne window boundries --- different on each machine
win_w = s.window_width()
win_h = s.window_height()

# --- Sette grensene for koordinatsystemet
max_x = win_w/2
min_x = win_w/2 * (-1)
max_y = win_h/2
min_y = win_h/2 * (-1)

# --- Koordinatene til midtpunktet i hver rute ---
""" Brukes til å bestemme plassering av figurer som skal 
     tegnes etter hvert tastetrykk 1 - 9 """
midtirute = { 
                1 : [min_x + (3/10*win_w), min_y + (7/10*win_h)],
                2 : [min_x + (5/10*win_w), min_y + (7/10*win_h)],
                3 : [min_x + (7/10*win_w), min_y + (7/10*win_h)],
                4 : [min_x + (3/10*win_w), min_y + (5/10*win_h)],
                5 : [min_x + (5/10*win_w), min_y + (5/10*win_h)],
                6 : [min_x + (7/10*win_w), min_y + (5/10*win_h)],
                7 : [min_x + (3/10*win_w), min_y + (3/10*win_h)],
                8 : [min_x + (5/10*win_w), min_y + (3/10*win_h)],
                9 : [min_x + (7/10*win_w), min_y + (3/10*win_h)]
            }

# 1. Tegne grid
def tegne_grid():
    """  Jeg har gjort endringer for at spillet skal 
          kunne skalere riktig uansett window-size.
           Derfor bruker jeg relative koordinater, istedet for
            absolutte kooordinater.
             Siden det skal være 3 streker i Tic Tac toe så er skjermen
              delt inn i 3 deler. Hver del er 1/3 av window height og width.
               Jeg har også valgt at grensene rundt kanten på spillet, tilsvarer
                1/10 av window heigt og width.
                 Derfor må strekene som turtle tegner være 8/10 av win height og width.
                  Dersom en ønsker å gjøre plass på skjermen til andre ting, som f.eks informasjon
                   om poengsum og navn, så er det lett å gjøre endringer.
                    F.eks dele opp skjermen i 1/4-deler i stedet, for så å tegneTicTactoe på 3/4 
                     av skjermen, info på den siste 1/4-delen, osv osv.
     ---------------------------------------------------------- Jonas ------------------------------ """

    # --- Tegner TicTacToe-streker med relative koordinater ---
    t.penup()
    t.setpos(min_x + (3/5*win_w), max_y - (1/5*win_h))
    t.setheading(270)
    t.pendown()
    t.forward(3/5*win_h)

    t.penup()
    t.setpos(max_x - (1/5*win_w), min_y + (2/5*win_h))
    t.setheading(180)
    t.pendown()
    t.forward(3/5*win_w)

    t.penup()
    t.setpos(min_x + (2/5*win_w), max_y - (1/5*win_h))
    t.setheading(270)
    t.pendown()
    t.forward(3/5*win_h)

    t.penup()
    t.setpos(min_x + (1/5*win_w), min_y + (3/5*win_h))
    t.setheading(0)
    t.pendown()
    t.forward(3/5*win_w)


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
            t.goto(min_x + (win_w*1.1/5) + (win_w*1/5*k),
                   max_y - (win_h*1.1/5) - (win_h*1/5*i))
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

    # 1. endret variabel 'spiller' til 'player' for å unngå 'shadowing in outer scope'
    # 2. lagt til variabel neste_player slik at vi kan svitsje mellom spillere

    # ---------------------------------------raglew---------------------------------

    player = random.randrange(1, 3)
    if player == 1:
        next_player = 2
        print("Spiller %s starter." % player)                                           # debug data
    else:
        player = 2
        next_player = 1
        print("Spiller %s starter." % player)                                           # debug data
    return player, next_player


def hvem_sin_tur(player):
    """ Denne funksjonen skriver en tekst oppe i venstre 
         hjørnet av spillet, som viser hvem sin tur det er. 
          Håpet er at denne skal oppdatere seg selv, etterhvert 
           som spillet uvikler seg. Annenhver gang skal den skrive 
            Spiller 1 og annenhver spiller 2.                   
    -------------------------------------------------- Jonas ----  """
    # endret fra 't' turtle til 'i' turtle for å unngå mulige konflikt     ---- raglew

    # clear før neste 'hvem_sin_tur' skrives ut
    i.clear()
    # nyttig å bruke farge til gjeldene spiller :)
    i.color(farge)
    i.goto(min_x + (win_w * 0.5/10), max_y - (win_h * 0.7/10))
    i.pendown()
    i.write("Spiller %d sin tur" % player, move=False, align="left",
            font=("Arial", 15, "bold"))



def tegn_stamp1():
    tegn_stamp(1)


def tegn_stamp2():
    tegn_stamp(2)


def tegn_stamp3():
    tegn_stamp(3)


def tegn_stamp4():
    tegn_stamp(4)


def tegn_stamp5():
    tegn_stamp(5)


def tegn_stamp6():
    tegn_stamp(6)


def tegn_stamp7():
    tegn_stamp(7)


def tegn_stamp8():
    tegn_stamp(8)


def tegn_stamp9():  
    tegn_stamp(9)


def tegn_stamp(rute):
    global spiller
    rute_x, rute_y = midtirute[rute]
    if spiller == 1:
        f.color("red")
        f.setpos(rute_x, rute_y)
        f.stamp()
        spiller = 2
        hvem_sin_tur(2)
    else:
        f.color("green")
        f.setpos(rute_x, rute_y)
        f.stamp()
        spiller = 1
        hvem_sin_tur(1)



# Init graphics and logics
tegne_grid()
tegne_rutenummer()

spiller, neste_spiller = hvem_starter()
print('spiller, neste spiller', spiller, neste_spiller)
# --- Main game ----

s.onkey(tegn_stamp1, ("1")) 
s.onkey(tegn_stamp2, ("2"))
s.onkey(tegn_stamp3, ("3"))
s.onkey(tegn_stamp4, ("4"))
s.onkey(tegn_stamp5, ("5"))
s.onkey(tegn_stamp6, ("6"))
s.onkey(tegn_stamp7, ("7"))
s.onkey(tegn_stamp8, ("8"))
s.onkey(tegn_stamp9, ("9"))
s.listen()

hvem_sin_tur(spiller)

s.mainloop()


# 2. Spiller 1 plassere
# 3. Spiller 2 plassere
# 4. Inn til en av spillene winner

# Disse funksjonene må være med for at programmet skal fungere.


"""
    Session 
    22:05
    - Lagt til funksjoner til tastene 1-9 som tegner en sirkel i 
     rute 1 - 9. 
    - Lagt til midtrute = {} med koordinatene til midtpunktet i alle rutene.
    - Endret inndelingen av vinduet fra 1/3-deler til 1/5 deler.

"""