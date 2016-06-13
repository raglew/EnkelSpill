#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------  Tic Tac Toe med 2 spillere

# -------------------  Authors: EmilZach, Arxcis, raglew


from turtle import *
# import vlc
import random
import time

# Init turtle
t = Turtle()
s = Screen()
f = Turtle()                     # f = figur, for å tegne figur etter spillerens klikk -- raglew
i = Turtle()                     # i = instruks, for å endre instruks i hvem_sin_tur funksjon -- raglew
w = Turtle()                     # w = warning, skriver warning dersom en rute er opptatt --Jonas 
p1 = Turtle()                    # p1 = vise poengene til player 1
p2 = Turtle()                    # p2 = vise poengene til player 2

# ------------------  KONSTANTER   -------------------------------

win_w = s.window_width()         # Forskjellig for hver maskin
win_h = s.window_height()        # -----------// -------------

# --- Sette grensene for koordinatsystemet ---
max_x = win_w/2
min_x = win_w/2 * (-1)
max_y = win_h/2
min_y = win_h/2 * (-1)

# --- Koordinatene til midtpunktet i hver rute --- Jonas
# --- Brukes til å plassere f.stamp() i midten av rutene ---
midtirute = {   7 : [min_x + (3/10*win_w), min_y + (7/10*win_h)],
                8 : [min_x + (5/10*win_w), min_y + (7/10*win_h)],
                9 : [min_x + (7/10*win_w), min_y + (7/10*win_h)],
                4 : [min_x + (3/10*win_w), min_y + (5/10*win_h)],
                5 : [min_x + (5/10*win_w), min_y + (5/10*win_h)],
                6 : [min_x + (7/10*win_w), min_y + (5/10*win_h)],
                1 : [min_x + (3/10*win_w), min_y + (3/10*win_h)],
                2 : [min_x + (5/10*win_w), min_y + (3/10*win_h)],
                3 : [min_x + (7/10*win_w), min_y + (3/10*win_h)]   }

# --------------- GLOBALE VARIABLER -------------------------------
opptatt_rute = []
rutefarger = {}
spillerne = {}
spiller, neste_spiller = 0, 0
farge = ""
spilleren = ""
counter = 0
poeng1 = 0
poeng2 = 0

# ----------------- FUNKSJONER --------------------------

def init_turtles():
    # ----------------- Graphics turtle -------------
    t.speed(8)
    t.st()
    # -------------------init figur turtle  ------------  raglew
    f.ht()
    f.speed(0)
    f.shape('circle')                        # sirkel som test
    farge = 'red'                            # variabel som kan brukes i svitsj_spiller funksjon
    f.color(farge)                           # rød farge som test
    f.turtlesize(5)
    f.penup()
    # -------------------init instruks turtle ------------raglew
    i.ht()
    i.speed(0)
    i.penup()
    i.shape('circle')
    i.turtlesize(3)
    # ---------------Init warning turtle -------------Jonas
    w.ht()
    w.speed(0)
    w.color("Orange")
    # -------- ----- init poeng turtles ------- Jonas
    p1.ht()
    p1.speed(0)
    p1.penup()
    p1.goto(min_x + (0.68/10*win_w), min_y + (5.98/10*win_h))
    p1.seth(90)
    p1.color("red")
    p1.pendown()
    p1.showturtle()
    p1.width(2)

    p2.ht()
    p2.speed(0)
    p2.penup()
    p2.goto(min_x + (0.68/10*win_w), min_y + (3.98/10*win_h))
    p2.seth(90)
    p2.color("green")
    p2.pendown()
    p2.showturtle()
    p2.width(2)


def reset_turtles():
    # --- Nullstille turtles ---
    t.reset()
    t.ht()
    f.reset()
    f.ht()
    i.reset()
    i.ht()
    w.reset()
    w.ht()
    p1.reset()
    p1.ht()
    p2.reset()
    p2.ht()


def tegne_grid():
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

    # Instruks om hvordan man avslutter spillet
    t.penup()
    t.setpos(0, min_y + (1/10*win_h))
    t.write("Avslutte?   <mellomrom>", move=False, align="center",
            font=("Arial", 15, "bold"))

    # Tegner poeng
    t.goto(min_x + (1/10*win_w), min_y + (5.75/10*win_h))
    t.write(poeng1, move=False, align="center", 
            font=("Arial", 20, "normal"))
    t.goto(min_x + (1/10*win_w), min_y + (3.75/10*win_h))
    t.write(poeng2, move=False, align="center", 
            font=("Arial", 20, "normal"))



def tegne_rutenummer():
    """ Her skal vi tilegne hver rute i spillet et tall.
         Slik at spilleren vet hvilken tast han/hun skal 
          bruke for å skrive et kryss eller sirkel i den 
           bestemte ruten.
    --------------------------------------- Jonas ----- """    
    # Først en liste med tall fra 1, 9
    liste = [7, 8, 9, 4, 5, 6, 1, 2, 3]
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
    t.ht()
    

def hvem_starter(player, nexplayer):
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
        nexplayer = 2
        print("Spiller %s starter." % player)                               # debug data
    else:
        player = 2
        nexplayer = 1
        print("Spiller %s starter." % player)                               # debug data
    return player, nexplayer


def hvem_sin_tur():
    """ Denne funksjonen skriver en tekst oppe i venstre 
         hjørnet av spillet, som viser hvem sin tur det er. 
          Håpet er at denne skal oppdatere seg selv, etterhvert 
           som spillet uvikler seg. Annenhver gang skal den skrive 
            Spiller 1 og annenhver spiller 2.                   
    -------------------------------------------------- Jonas ----  """

    # clear før neste 'hvem_sin_tur' skrives ut
    i.clear()
    # nyttig å bruke farge til gjeldene spiller :)
    i.color(farge)
    i.goto(min_x + (win_w * 0.5/10), max_y - (win_h * 1.2/10))
    spilleren = spillerne[spiller]
    i.write("Din tur %s" % spilleren, move=False, align="left",
            font=("Arial", 20, "bold"))
    # - Added big circle in right corner
    i.goto(max_x - (win_w * 1/10), max_y - (win_h * 1/10))
    i.stamp()


def svitsj_spillere():
    # --------  funksjon for å svitsje spillere -----------------------  raglew

    global spiller, neste_spiller, farge
    spiller, neste_spiller = neste_spiller, spiller

    # svitsj også figurfarge
    if farge == 'red':
        farge = 'green'
        f.color(farge)
    elif farge == 'green':
        farge = 'red'
        f.color(farge)
    else:
        print('farge error')

    # den svisjet spilleren kan nå plassere
    hvem_sin_tur()


def plasser_stamp_onclick(x, y):
    """ Opprinnelig plassere() av raglew, modifisert av Jonas. 
         Denne funksjonen får posisjon fra et museklikk. 
          Så skjekkes differensen til midten av alle rutene, vha.
           "midtirute = {" og en for-løkke. Differansen lagres i 
             variabelen d, for hver løkke. Når "d" er liten nok, så 
       startes tegn_stamp() i den korresponderende ruten, og løkken brytes.
    ------------------------------------------ Raglew, Jonas --------- """
    for i in range(1,10):
        midt_x, midt_y = midtirute[i]
        # h = sqrt((x1-x2)^2 + (y1 - y2)^2)  Ref: Pytagoras
        d = ((((midt_x - x)**2) + ((midt_y - y)**2))**0.5) 
        if d < 50:                                      # Treshhold < 50
            tegn_stamp(i)                               # i = rutenummer
            break


def tegn_stamp(rute):
    """ Funksjonen får data om hvilken rute det skal tegnes i, og 
         henter posisjonen til midten av ruten utifra "midtirute = {", 
          som er definert i starten av programmet. Posisjon settes og
           det f.stamp()-es. Til slutt så startes svitsj_spillere().
            Update: Dersom ruten allerede er brukt, så vil funksjonen
             nekte å skrive noe, og starte tegn_opptatt().
    -------------------------------------------- Jonas ----- """
    global opptatt_rute
    if rute in opptatt_rute:                   # "Er ruten opptatt ?"
        vis_opptatt(rute)
        return 0
    else:
        opptatt_rute.append(rute)              # "Denne ruten er nå opptatt"

        midt_x, midt_y = midtirute[rute]
        f.setpos(midt_x, midt_y)
        f.color(farge)
        f.stamp()
        checkif_gameover(rute)


def checkif_gameover(rute):
    """ Skjekker om spillet er over
        # - If False: Spillet går videre
        # - If True:  Noen har vunnet
        # - Else:      Det ble uavgjort
      ---------------------- Jonas --- """
    if not vinn_eller_uavgjort(rute):
        svitsj_spillere()
    elif vinn_eller_uavgjort(rute):
        vis_victory()
        new_game()
    else:
        vis_uavgjort()
        new_game()
            

def vinn_eller_uavgjort(rute):
    """For å kåre vinner så lagrer vi hvilken spiller
        som har skrevet i hvilken rute, i rutefarger = {.
         Variabelen --> farge, representerer spilleren til en 
          hver tid. Spiller1 = 'red', Spiller2 = 'green'
           rute sendes videre fra tegn_stamp()
    ---------------------------------------Jonas--------"""
    global rutefarger, counter
    rutefarger[rute] = farge
    counter += 1
    # Sjekk horisontale linjer                                               
    for i in [0, 3, 6]:
        if rutefarger[1+i] == rutefarger[2+i] == rutefarger[3+i]:
            return True
    # Skjekk Vertikal linjer
    for i in [0, 1, 2]:
        if rutefarger[1+i] == rutefarger[4+i] == rutefarger[7+i]:
            return True
    # Skjekk Diagonal linjer
    for i in [0, 6]:
        if rutefarger[1+i] == rutefarger[5] == rutefarger[9-i]:
            return True
    # Dersom alle rutene er fulle
    if counter == 9:                
        return 2
    else:
        return False


def vis_opptatt(rute):
    """ Kjøres dersom ruten som blir forsøkt skrevet til i
         tegn_stamp(), allerede er registrert i listen opptatt_rute = []"""

    w.write("RUTE %d ER OPPTATT" % rute, move=False, align="center",
             font=("Arial", 40, "bold"))
    time.sleep(1.5)
    w.clear()


def vis_victory():
    """ Kjøres dersom vinn_eller_uavgjort() -> return True"""
    reset_turtles()
    gi_poeng()
    w.color(farge)
    spilleren = spillerne[spiller]
    w.write("%s har VUNNET!" % spilleren, move=False, align="center",
            font=("Arial", 40, "bold"))
    time.sleep(2)


def vis_uavgjort():
    """ Kjøres dersom vinn_eller_uavgjort() -> return 2"""
    reset_turtles()
    w.color(farge)
    w.write("DET BLE UAVJORT...", move=False, align="center",
            font=("Arial", 40, "bold"))
    time.sleep(2)


def gi_poeng():
    """ Kjøres når funksjonen vis_victory() kjøres"""
    global poeng1, poeng2
    if spiller == 1:
        poeng1 += 1
    elif spiller == 2:
        poeng2 += 1


def avslutter():
    # Avslutter spillet
    time.sleep(0.5)
    s.clear()
    w.color(farge)
    spilleren = spillerne[spiller]
    andre_spilleren = spillerne[neste_spiller]
    w.write("{} & {}".format(spilleren, andre_spilleren), move=False, align="center",
            font=("Arial", 30, "bold"))
    w.setpos(0, min_y + (1/3*win_h))
    w.write("Hade på bade din gamle sjokolade".format(spilleren, andre_spilleren), move=False, align="center",
            font=("Arial", 30, "bold"))
    time.sleep(3)
    s.bye()


def test_stamp_pick(tast):
    """ Denne funksjonen har fjernet 9 funksjoner. Basically så
    sørger den for å gi parameteren -> tast, til en funksjon
    som ikke kan ta i mot parametere i utganspunktet.
    --------------------------------- Jonas --------- """
    def tast_stamp():
        tegn_stamp(tast)
    return tast_stamp


def listen_clicks_keys():
    s.onclick(plasser_stamp_onclick) # --- Metode 1: Museklikk
    s.onkey(test_stamp_pick(1), ("1"))      # --- Metode 2: Num_pad
    s.onkey(test_stamp_pick(2), ("2"))
    s.onkey(test_stamp_pick(3), ("3"))
    s.onkey(test_stamp_pick(4), ("4"))
    s.onkey(test_stamp_pick(5), ("5"))
    s.onkey(test_stamp_pick(6), ("6"))
    s.onkey(test_stamp_pick(7), ("7"))
    s.onkey(test_stamp_pick(8), ("8"))
    s.onkey(test_stamp_pick(9), ("9"))
    s.onkey(avslutter, 'space')       # ---  avslutter med <mellomrom>
    s.listen()


def hent_navn():
    # Hent navner fra spillerne
    spiller_navn = s.textinput("1ste Spiller", "Navn til den første spilleren:")
    neste_spiller_navn = s.textinput("2ndre Spiller", "Navn til den andre spilleren:")
    # Endre små til stor bokstav
    spiller_navn = spiller_navn.upper()
    neste_spiller_navn = neste_spiller_navn.upper()
    # Legge navner til spillerne dictionary
    spillerne[1] = spiller_navn
    spillerne[2] = neste_spiller_navn


def while_game():
    """ Cool animation """
    while True:
    	p1.circle(-30, 5)
    	p2.circle(-30, 5)

def new_game():
    """ Den viktigste funksjonen av dem alle.
         Hovedoppgaven er å sørge for at utgangspunktet
          er helt likt hver gang et spill startes, slik
           at resten av funksjonene fungerer som de skal.
           ------------------------------------------ """
    global spiller, neste_spiller, opptatt_rute, rutefarger, farge, counter
    # --- Nullstille turtles ---
    reset_turtles()
    # --- Nullstille variabler ---
    opptatt_rute = []
    rutefarger = {7: "farge7", 8: "farge8", 9: "farge9",
                  4: "farge4", 5: "farge5", 6: "farge6",
                  1: "farge1", 2: "farge2", 3: "farge3"}
    counter = 0
    # --- Init logics ---
    spiller, neste_spiller = hvem_starter(spiller, neste_spiller)
    if spiller == 1: 
        farge = "red"
    elif spiller == 2: 
        farge = "green"
    # --- Init turtles ---
    init_turtles()
    # --- Init graphics ---
    tegne_grid()
    tegne_rutenummer()
    hvem_sin_tur()
    # --- Init event listening ---
    listen_clicks_keys()
    # --- While loop ---
    while_game()

# MAIN
hent_navn()
# p = vlc.MediaPlayer("Hot_Butter-Popcorn.mp3")
# p.play()
new_game()

s.mainloop()


"""
    Issue: Turtles forsvinner når new_game() startes for 2. gang.
          + de tegnes ikke skikkelig.

    Løsningen for nå: Unngå å bruke VLC biblioteket. Det er den som får programmet til å kræsje når man skal spille lyd / musikk.
"""
