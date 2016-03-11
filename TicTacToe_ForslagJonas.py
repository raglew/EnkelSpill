"""


    Tittel: TicTacToe_ForslagJonas.py
    Opprettet: 16:52 - 11.03.2016
    Author: Jonas J. Solsvik
    Beskrivelse: Dette er en tekstfil, hvor jeg tester ut endringsforslag til TicTacToe.py.
                  Det vil være opp til hovedforfattere av TicTacToe.py om de ønsker å "merge" noen
                   av endringsforslagene mine. Jeg kommer ikke til å legge meg bort i det.

                                                                      Takk, Jonas

"""

from turtle import *    # --- endret Jonas
import random

# Init turtle
t = Turtle()
s = Screen()


# 1. Tegne grid
def tegne_grid():
    """ --- Jeg har gjort endringer for at spillet skal 
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



# 2. Spiller 1 plassere
# 3. Spiller 2 plassere
# 4. Inn til en av spillene winner

# Disse funksjonene må være med for at programmet skal fungere.

tegne_grid()
s.listen()

s.mainloop()
