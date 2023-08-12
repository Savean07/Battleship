import turtle as t
import random

#-----setup-----
wn = t.Screen()
wn.tracer(False)
wn.setup(width=1.0, height=1.0)
wn.bgcolor("deepskyblue2")
font_setup = ("Times New Roman", 30, "bold")
back2 = t.Turtle()
back2.pu()
back2.hideturtle()
t.update()
start = "start.gif"
a = "board.gif"
miss = "miss.gif"
hit = "hit.gif"
tts = "tt.gif"
wn.addshape(start)
wn.addshape(a)
wn.addshape(miss)
wn.addshape(hit)
wn.addshape(tts)
t.hideturtle()
t.pensize(5)
t.update()

loop = True
loop2 = True

def start_game(x, y):
  back2.hideturtle()
  global loop2
  global loop
  loop = False
  loop2 = False
  t.update()

while loop2:
  back2.showturtle()
  back2.shape(start)
  back2.onclick(start_game)
  t.update()

y = 315
x = -325
y2 = 285
x2 = -292
turns = 49
tempInt = 0
ship_spots_left = 17
ship_row = random.randint(4, 5)
ship_column = random.randint(4, 5)
bd = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

destroyer = 2
submarine = 3
cruiser = 3
battleship = 4
aircraftCarrier = 5

a1 = False
a2 = False
a3 = False
a4 = False
a5 = False
a6 = False
a7 = False
a8 = False
a9 = False
a10 = False
b1 = False
b2 = False
b3 = False
b4 = False
b5 = False
b6 = False
b7 = False
b8 = False
b9 = False
b10 = False
c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
c6 = False
c7 = False
c8 = False
c9 = False
c10 = False
d1 = False
d2 = False
d3 = False
d4 = False
d5 = False
d6 = False
d7 = False
d8 = False
d9 = False
d10 = False
e1 = False
e2 = False
e3 = False
e4 = False
e5 = False
e6 = False
e7 = False
e8 = False
e9 = False
e10 = False
f1 = False
f2 = False
f3 = False
f4 = False
f5 = False
f6 = False
f7 = False
f8 = False
f9 = False
f10 = False
g1 = False
g2 = False
g3 = False
g4 = False
g5 = False
g6 = False
g7 = False
g8 = False
g9 = False
g10 = False
h1 = False
h2 = False
h3 = False
h4 = False
h5 = False
h6 = False
h7 = False
h8 = False
h9 = False
h10 = False
i1 = False
i2 = False
i3 = False
i4 = False
i5 = False
i6 = False
i7 = False
i8 = False
i9 = False
i10 = False
j1 = False
j2 = False
j3 = False
j4 = False
j5 = False
j6 = False
j7 = False
j8 = False
j9 = False
j10 = False

board = t.Turtle()
board.shape(a)
board.back(15)
board.stamp()
board.hideturtle()

turn_writer = t.Turtle()
turn_writer.pencolor("white")
turn_writer.pu()
turn_writer.hideturtle()
turn_writer2 = t.Turtle()
turn_writer2.pencolor("white")
turn_writer2.pu()
turn_writer2.hideturtle()
turn_writer2.goto(-175, 460)
turn_writer2.write("Turns Left:", font=font_setup)
turn_writer.goto(85, 460)
turn_writer.write("50", font=font_setup)

def game_over_win():
  t.tracer(False)
  A1.clear()
  A2.clear()
  A3.clear()
  A4.clear()
  A5.clear()
  A6.clear()
  A7.clear()
  A8.clear()
  A9.clear()
  A10.clear()
  B1.clear()
  B2.clear()
  B3.clear()
  B4.clear()
  B5.clear()
  B6.clear()
  B7.clear()
  B8.clear()
  B9.clear()
  B10.clear()
  C1.clear()
  C2.clear()
  C3.clear()
  C4.clear()
  C5.clear()
  C6.clear()
  C7.clear()
  C8.clear()
  C9.clear()
  C10.clear()
  D1.clear()
  D2.clear()
  D3.clear()
  D4.clear()
  D5.clear()
  D6.clear()
  D7.clear()
  D8.clear()
  D9.clear()
  D10.clear()
  E1.clear()
  E2.clear()
  E3.clear()
  E4.clear()
  E5.clear()
  E6.clear()
  E7.clear()
  E8.clear()
  E9.clear()
  E10.clear()
  F1.clear()
  F2.clear()
  F3.clear()
  F4.clear()
  F5.clear()
  F6.clear()
  F7.clear()
  F8.clear()
  F9.clear()
  F10.clear()
  G1.clear()
  G2.clear()
  G3.clear()
  G4.clear()
  G5.clear()
  G6.clear()
  G7.clear()
  G8.clear()
  G9.clear()
  G10.clear()
  H1.clear()
  H2.clear()
  H3.clear()
  H4.clear()
  H5.clear()
  H6.clear()
  H7.clear()
  H8.clear()
  H9.clear()
  H10.clear()
  I1.clear()
  I2.clear()
  I3.clear()
  I4.clear()
  I5.clear()
  I6.clear()
  I7.clear()
  I8.clear()
  I9.clear()
  I10.clear()
  J1.clear()
  J2.clear()
  J3.clear()
  J4.clear()
  J5.clear()
  J6.clear()
  J7.clear()
  J8.clear()
  J9.clear()
  J10.clear()
  A1.hideturtle()
  A2.hideturtle()
  A3.hideturtle()
  A4.hideturtle()
  A5.hideturtle()
  A6.hideturtle()
  A7.hideturtle()
  A8.hideturtle()
  A9.hideturtle()
  A10.hideturtle()
  B1.hideturtle()
  B2.hideturtle()
  B3.hideturtle()
  B4.hideturtle()
  B5.hideturtle()
  B6.hideturtle()
  B7.hideturtle()
  B8.hideturtle()
  B9.hideturtle()
  B10.hideturtle()
  C1.hideturtle()
  C2.hideturtle()
  C3.hideturtle()
  C4.hideturtle()
  C5.hideturtle()
  C6.hideturtle()
  C8.hideturtle()
  C9.hideturtle()
  C10.hideturtle()
  D1.hideturtle()
  D2.hideturtle()
  D3.hideturtle()
  D4.hideturtle()
  D5.hideturtle()
  D6.hideturtle()
  D7.hideturtle()
  D8.hideturtle()
  D9.hideturtle()
  D10.hideturtle()
  E1.hideturtle()
  E2.hideturtle()
  E3.hideturtle()
  E4.hideturtle()
  E5.hideturtle()
  E6.hideturtle()
  E7.hideturtle()
  E8.hideturtle()
  E9.hideturtle()
  E10.hideturtle()
  F1.hideturtle()
  F2.hideturtle()
  F3.hideturtle()
  F4.hideturtle()
  F5.hideturtle()
  F6.hideturtle()
  F7.hideturtle()
  F8.hideturtle()
  F9.hideturtle()
  F10.hideturtle()
  G1.hideturtle()
  G2.hideturtle()
  G3.hideturtle()
  G4.hideturtle()
  G5.hideturtle()
  G6.hideturtle()
  G6.hideturtle()
  G7.hideturtle()
  G8.hideturtle()
  G9.hideturtle()
  G10.hideturtle()
  H1.hideturtle()
  H2.hideturtle()
  H3.hideturtle()
  H4.hideturtle()
  H5.hideturtle()
  H6.hideturtle()
  H7.hideturtle()
  H8.hideturtle()
  H9.hideturtle()
  H10.hideturtle()
  I1.hideturtle()
  I2.hideturtle()
  I3.hideturtle()
  I4.hideturtle()
  I5.hideturtle()
  I6.hideturtle()
  I7.hideturtle()
  I8.hideturtle()
  I9.hideturtle()
  I10.hideturtle()
  J1.hideturtle()
  J2.hideturtle()
  J3.hideturtle()
  J4.hideturtle()
  J5.hideturtle()
  J6.hideturtle()
  J7.hideturtle()
  J8.hideturtle()
  J9.hideturtle()
  J10.hideturtle()
  t.update()
  t.tracer(True)
  while loop == False:
    t.tracer(False)
    back2.clear()
    turn_writer.clear()
    turn_writer2.clear()
    t.clear()
    turn_writer.goto(-280, -40)
    turn_writer.write("You Sunk All The Ships", font=font_setup)
    turn_writer.goto(-155, 10)
    turn_writer.write("Game Over!", font=font_setup)
    t.update()

def game_over_lose():
  t.tracer(False)
  A1.clear()
  A2.clear()
  A3.clear()
  A4.clear()
  A5.clear()
  A6.clear()
  A7.clear()
  A8.clear()
  A9.clear()
  A10.clear()
  B1.clear()
  B2.clear()
  B3.clear()
  B4.clear()
  B5.clear()
  B6.clear()
  B7.clear()
  B8.clear()
  B9.clear()
  B10.clear()
  C1.clear()
  C2.clear()
  C3.clear()
  C4.clear()
  C5.clear()
  C6.clear()
  C7.clear()
  C8.clear()
  C9.clear()
  C10.clear()
  D1.clear()
  D2.clear()
  D3.clear()
  D4.clear()
  D5.clear()
  D6.clear()
  D7.clear()
  D8.clear()
  D9.clear()
  D10.clear()
  E1.clear()
  E2.clear()
  E3.clear()
  E4.clear()
  E5.clear()
  E6.clear()
  E7.clear()
  E8.clear()
  E9.clear()
  E10.clear()
  F1.clear()
  F2.clear()
  F3.clear()
  F4.clear()
  F5.clear()
  F6.clear()
  F7.clear()
  F8.clear()
  F9.clear()
  F10.clear()
  G1.clear()
  G2.clear()
  G3.clear()
  G4.clear()
  G5.clear()
  G6.clear()
  G7.clear()
  G8.clear()
  G9.clear()
  G10.clear()
  H1.clear()
  H2.clear()
  H3.clear()
  H4.clear()
  H5.clear()
  H6.clear()
  H7.clear()
  H8.clear()
  H9.clear()
  H10.clear()
  I1.clear()
  I2.clear()
  I3.clear()
  I4.clear()
  I5.clear()
  I6.clear()
  I7.clear()
  I8.clear()
  I9.clear()
  I10.clear()
  J1.clear()
  J2.clear()
  J3.clear()
  J4.clear()
  J5.clear()
  J6.clear()
  J7.clear()
  J8.clear()
  J9.clear()
  J10.clear()
  A1.hideturtle()
  A2.hideturtle()
  A3.hideturtle()
  A4.hideturtle()
  A5.hideturtle()
  A6.hideturtle()
  A7.hideturtle()
  A8.hideturtle()
  A9.hideturtle()
  A10.hideturtle()
  B1.hideturtle()
  B2.hideturtle()
  B3.hideturtle()
  B4.hideturtle()
  B5.hideturtle()
  B6.hideturtle()
  B7.hideturtle()
  B8.hideturtle()
  B9.hideturtle()
  B10.hideturtle()
  C1.hideturtle()
  C2.hideturtle()
  C3.hideturtle()
  C4.hideturtle()
  C5.hideturtle()
  C6.hideturtle()
  C8.hideturtle()
  C9.hideturtle()
  C10.hideturtle()
  D1.hideturtle()
  D2.hideturtle()
  D3.hideturtle()
  D4.hideturtle()
  D5.hideturtle()
  D6.hideturtle()
  D7.hideturtle()
  D8.hideturtle()
  D9.hideturtle()
  D10.hideturtle()
  E1.hideturtle()
  E2.hideturtle()
  E3.hideturtle()
  E4.hideturtle()
  E5.hideturtle()
  E6.hideturtle()
  E7.hideturtle()
  E8.hideturtle()
  E9.hideturtle()
  E10.hideturtle()
  F1.hideturtle()
  F2.hideturtle()
  F3.hideturtle()
  F4.hideturtle()
  F5.hideturtle()
  F6.hideturtle()
  F7.hideturtle()
  F8.hideturtle()
  F9.hideturtle()
  F10.hideturtle()
  G1.hideturtle()
  G2.hideturtle()
  G3.hideturtle()
  G4.hideturtle()
  G5.hideturtle()
  G6.hideturtle()
  G6.hideturtle()
  G7.hideturtle()
  G8.hideturtle()
  G9.hideturtle()
  G10.hideturtle()
  H1.hideturtle()
  H2.hideturtle()
  H3.hideturtle()
  H4.hideturtle()
  H5.hideturtle()
  H6.hideturtle()
  H7.hideturtle()
  H8.hideturtle()
  H9.hideturtle()
  H10.hideturtle()
  I1.hideturtle()
  I2.hideturtle()
  I3.hideturtle()
  I4.hideturtle()
  I5.hideturtle()
  I6.hideturtle()
  I7.hideturtle()
  I8.hideturtle()
  I9.hideturtle()
  I10.hideturtle()
  J1.hideturtle()
  J2.hideturtle()
  J3.hideturtle()
  J4.hideturtle()
  J5.hideturtle()
  J6.hideturtle()
  J7.hideturtle()
  J8.hideturtle()
  J9.hideturtle()
  J10.hideturtle()
  t.update()
  while loop == False:
    t.tracer(False)
    back2.clear()
    turn_writer.clear()
    turn_writer2.clear()
    t.clear()
    turn_writer.goto(-280, -40)
    turn_writer.write("You Ran Out Of Turns", font=font_setup)
    turn_writer.goto(-160, 10)
    turn_writer.write("Game Over!", font=font_setup)
    t.update()
  
def update_turnsleft():
  global turns
  if turns > 0 and ship_spots_left > 0:
    turn_writer.clear()
    turn_writer.write(turns, font=font_setup)
  if ship_spots_left == 0 and turns > 0:
    game_over_win()
  if ship_spots_left > 0 and turns == 0:
    game_over_lose()
  turns -= 1
  
def create_spots():
  global A1
  global A2
  global A3
  global A4
  global A5
  global A6
  global A7
  global A8
  global A9
  global A10
  global B1
  global B2
  global B3
  global B4
  global B5
  global B6
  global B7
  global B8
  global B9
  global B10
  global C1
  global C2
  global C3
  global C4
  global C5
  global C6
  global C7
  global C8
  global C9
  global C10
  global D1
  global D2
  global D3
  global D4
  global D5
  global D6
  global D7
  global D8
  global D9
  global D10
  global E1
  global E2
  global E3
  global E4
  global E5
  global E6
  global E7
  global E8
  global E9
  global E10
  global F1
  global F2
  global F3
  global F4
  global F5
  global F6
  global F7
  global F8
  global F9
  global F10
  global G1
  global G2
  global G3
  global G4
  global G5
  global G6
  global G7
  global G8
  global G9
  global G10
  global H1
  global H2
  global H3
  global H4
  global H5
  global H6
  global H7
  global H8
  global H9
  global H10
  global I1
  global I2
  global I3
  global I4
  global I5
  global I6
  global I7
  global I8
  global I9
  global I10
  global J1
  global J2
  global J3
  global J4
  global J5
  global J6
  global J7
  global J8
  global J9
  global J10

  A1 = t.Turtle()
  A1.shape(tts)
  A1.pu()
  A1.goto(x2, y2)

  A2 = t.Turtle()
  A2.shape(tts)
  A2.pu()
  A2.goto(x2 + 65, y2)

  A3 = t.Turtle()
  A3.shape(tts)
  A3.pu()
  A3.goto(x2 + 130, y2)

  A4 = t.Turtle()
  A4.shape(tts)
  A4.pu()
  A4.goto(x2 + 195, y2)

  A5 = t.Turtle()
  A5.shape(tts)
  A5.pu()
  A5.goto(x2 + 260, y2)

  A6 = t.Turtle()
  A6.shape(tts)
  A6.pu()
  A6.goto(x2 + 325, y2)

  A7 = t.Turtle()
  A7.shape(tts)
  A7.pu()
  A7.goto(x2 + 390, y2)

  A8 = t.Turtle()
  A8.shape(tts)
  A8.pu()
  A8.goto(x2 + 455, y2)

  A9 = t.Turtle()
  A9.shape(tts)
  A9.pu()
  A9.goto(x2 + 520, y2)

  A10 = t.Turtle()
  A10.shape(tts)
  A10.pu()
  A10.goto(x2 + 585, y2)

  B1 = t.Turtle()
  B1.shape(tts)
  B1.pu()
  B1.goto(x2, y2 - 65)

  B2 = t.Turtle()
  B2.shape(tts)
  B2.pu()
  B2.goto(x2 + 65, y2 - 65)

  B3 = t.Turtle()
  B3.shape(tts)
  B3.pu()
  B3.goto(x2 + 130, y2 - 65)

  B4 = t.Turtle()
  B4.shape(tts)
  B4.pu()
  B4.goto(x2 + 195, y2 - 65)

  B5 = t.Turtle()
  B5.shape(tts)
  B5.pu()
  B5.goto(x2 + 260, y2 - 65)

  B6 = t.Turtle()
  B6.shape(tts)
  B6.pu()
  B6.goto(x2 + 325, y2 - 65)

  B7 = t.Turtle()
  B7.shape(tts)
  B7.pu()
  B7.goto(x2 + 390, y2 - 65)

  B8 = t.Turtle()
  B8.shape(tts)
  B8.pu()
  B8.goto(x2 + 455, y2 - 65)

  B9 = t.Turtle()
  B9.shape(tts)
  B9.pu()
  B9.goto(x2 + 520, y2 - 65)

  B10 = t.Turtle()
  B10.shape(tts)
  B10.pu()
  B10.goto(x2 + 585, y2 - 65)

  C1 = t.Turtle()
  C1.shape(tts)
  C1.pu()
  C1.goto(x2, y2 - 130)

  C2 = t.Turtle()
  C2.shape(tts)
  C2.pu()
  C2.goto(x2 + 65, y2 - 130)

  C3 = t.Turtle()
  C3.shape(tts)
  C3.pu()
  C3.goto(x2 + 130, y2 - 130)

  C4 = t.Turtle()
  C4.shape(tts)
  C4.pu()
  C4.goto(x2 + 195, y2 - 130)

  C5 = t.Turtle()
  C5.shape(tts)
  C5.pu()
  C5.goto(x2 + 260, y2 - 130)

  C6 = t.Turtle()
  C6.shape(tts)
  C6.pu()
  C6.goto(x2 + 325, y2 - 130)

  C7 = t.Turtle()
  C7.shape(tts)
  C7.pu()
  C7.goto(x2 + 390, y2 - 130)

  C8 = t.Turtle()
  C8.shape(tts)
  C8.pu()
  C8.goto(x2 + 455, y2 - 130)

  C9 = t.Turtle()
  C9.shape(tts)
  C9.pu()
  C9.goto(x2 + 520, y2 - 130)

  C10 = t.Turtle()
  C10.shape(tts)
  C10.pu()
  C10.goto(x2 + 585, y2 - 130)

  D1 = t.Turtle()
  D1.shape(tts)
  D1.pu()
  D1.goto(x2, y2 - 195)

  D2 = t.Turtle()
  D2.shape(tts)
  D2.pu()
  D2.goto(x2 + 65, y2 - 195)

  D3 = t.Turtle()
  D3.shape(tts)
  D3.pu()
  D3.goto(x2 + 130, y2 - 195)

  D4 = t.Turtle()
  D4.shape(tts)
  D4.pu()
  D4.goto(x2 + 195, y2 - 195)

  D5 = t.Turtle()
  D5.shape(tts)
  D5.pu()
  D5.goto(x2 + 260, y2 - 195)

  D6 = t.Turtle()
  D6.shape(tts)
  D6.pu()
  D6.goto(x2 + 325, y2 - 195)

  D7 = t.Turtle()
  D7.shape(tts)
  D7.pu()
  D7.goto(x2 + 390, y2 - 195)

  D8 = t.Turtle()
  D8.shape(tts)
  D8.pu()
  D8.goto(x2 + 455, y2 - 195)

  D9 = t.Turtle()
  D9.shape(tts)
  D9.pu()
  D9.goto(x2 + 520, y2 - 195)

  D10 = t.Turtle()
  D10.shape(tts)
  D10.pu()
  D10.goto(x2 + 585, y2 - 195)

  E1 = t.Turtle()
  E1.shape(tts)
  E1.pu()
  E1.goto(x2, y2 - 260)

  E2 = t.Turtle()
  E2.shape(tts)
  E2.pu()
  E2.goto(x2 + 65, y2 - 260)

  E3 = t.Turtle()
  E3.shape(tts)
  E3.pu()
  E3.goto(x2 + 130, y2 - 260)

  E4 = t.Turtle()
  E4.shape(tts)
  E4.pu()
  E4.goto(x2 + 195, y2 - 260)

  E5 = t.Turtle()
  E5.shape(tts)
  E5.pu()
  E5.goto(x2 + 260, y2 - 260)

  E6 = t.Turtle()
  E6.shape(tts)
  E6.pu()
  E6.goto(x2 + 325, y2 - 260)

  E7 = t.Turtle()
  E7.shape(tts)
  E7.pu()
  E7.goto(x2 + 390, y2 - 260)

  E8 = t.Turtle()
  E8.shape(tts)
  E8.pu()
  E8.goto(x2 + 455, y2 - 260)

  E9 = t.Turtle()
  E9.shape(tts)
  E9.pu()
  E9.goto(x2 + 520, y2 - 260)

  E10 = t.Turtle()
  E10.shape(tts)
  E10.pu()
  E10.goto(x2 + 585, y2 - 260)

  F1 = t.Turtle()
  F1.shape(tts)
  F1.pu()
  F1.goto(x2, y2 - 325)

  F2 = t.Turtle()
  F2.shape(tts)
  F2.pu()
  F2.goto(x2 + 65, y2 - 325)

  F3 = t.Turtle()
  F3.shape(tts)
  F3.pu()
  F3.goto(x2 + 130, y2 - 325)

  F4 = t.Turtle()
  F4.shape(tts)
  F4.pu()
  F4.goto(x2 + 195, y2 - 325)

  F5 = t.Turtle()
  F5.shape(tts)
  F5.pu()
  F5.goto(x2 + 260, y2 - 325)

  F6 = t.Turtle()
  F6.shape(tts)
  F6.pu()
  F6.goto(x2 + 325, y2 - 325)

  F7 = t.Turtle()
  F7.shape(tts)
  F7.pu()
  F7.goto(x2 + 390, y2 - 325)

  F8 = t.Turtle()
  F8.shape(tts)
  F8.pu()
  F8.goto(x2 + 455, y2 - 325)

  F9 = t.Turtle()
  F9.shape(tts)
  F9.pu()
  F9.goto(x2 + 520, y2 - 325)

  F10 = t.Turtle()
  F10.shape(tts)
  F10.pu()
  F10.goto(x2 + 585, y2 - 325)

  G1 = t.Turtle()
  G1.shape(tts)
  G1.pu()
  G1.goto(x2, y2 - 390)

  G2 = t.Turtle()
  G2.shape(tts)
  G2.pu()
  G2.goto(x2 + 65, y2 - 390)

  G3 = t.Turtle()
  G3.shape(tts)
  G3.pu()
  G3.goto(x2 + 130, y2 - 390)

  G4 = t.Turtle()
  G4.shape(tts)
  G4.pu()
  G4.goto(x2 + 195, y2 - 390)

  G5 = t.Turtle()
  G5.shape(tts)
  G5.pu()
  G5.goto(x2 + 260, y2 - 390)

  G6 = t.Turtle()
  G6.shape(tts)
  G6.pu()
  G6.goto(x2 + 325, y2 - 390)

  G7 = t.Turtle()
  G7.shape(tts)
  G7.pu()
  G7.goto(x2 + 390, y2 - 390)

  G8 = t.Turtle()
  G8.shape(tts)
  G8.pu()
  G8.goto(x2 + 455, y2 - 390)

  G9 = t.Turtle()
  G9.shape(tts)
  G9.pu()
  G9.goto(x2 + 520, y2 - 390)

  G10 = t.Turtle()
  G10.shape(tts)
  G10.pu()
  G10.goto(x2 + 585, y2 - 390)

  H1 = t.Turtle()
  H1.shape(tts)
  H1.pu()
  H1.goto(x2, y2 - 455)

  H2 = t.Turtle()
  H2.shape(tts)
  H2.pu()
  H2.goto(x2 + 65, y2 - 455)

  H3 = t.Turtle()
  H3.shape(tts)
  H3.pu()
  H3.goto(x2 + 130, y2 - 455)

  H4 = t.Turtle()
  H4.shape(tts)
  H4.pu()
  H4.goto(x2 + 195, y2 - 455)

  H5 = t.Turtle()
  H5.shape(tts)
  H5.pu()
  H5.goto(x2 + 260, y2 - 455)

  H6 = t.Turtle()
  H6.shape(tts)
  H6.pu()
  H6.goto(x2 + 325, y2 - 455)

  H7 = t.Turtle()
  H7.shape(tts)
  H7.pu()
  H7.goto(x2 + 390, y2 - 455)

  H8 = t.Turtle()
  H8.shape(tts)
  H8.pu()
  H8.goto(x2 + 455, y2 - 455)

  H9 = t.Turtle()
  H9.shape(tts)
  H9.pu()
  H9.goto(x2 + 520, y2 - 455)

  H10 = t.Turtle()
  H10.shape(tts)
  H10.pu()
  H10.goto(x2 + 585, y2 - 455)

  I1 = t.Turtle()
  I1.shape(tts)
  I1.pu()
  I1.goto(x2, y2 - 520)

  I2 = t.Turtle()
  I2.shape(tts)
  I2.pu()
  I2.goto(x2 + 65, y2 - 520)

  I3 = t.Turtle()
  I3.shape(tts)
  I3.pu()
  I3.goto(x2 + 130, y2 - 520)

  I4 = t.Turtle()
  I4.shape(tts)
  I4.pu()
  I4.goto(x2 + 195, y2 - 520)

  I5 = t.Turtle()
  I5.shape(tts)
  I5.pu()
  I5.goto(x2 + 260, y2 - 520)

  I6 = t.Turtle()
  I6.shape(tts)
  I6.pu()
  I6.goto(x2 + 325, y2 - 520)

  I7 = t.Turtle()
  I7.shape(tts)
  I7.pu()
  I7.goto(x2 + 390, y2 - 520)

  I8 = t.Turtle()
  I8.shape(tts)
  I8.pu()
  I8.goto(x2 + 455, y2 - 520)

  I9 = t.Turtle()
  I9.shape(tts)
  I9.pu()
  I9.goto(x2 + 520, y2 - 520)

  I10 = t.Turtle()
  I10.shape(tts)
  I10.pu()
  I10.goto(x2 + 585, y2 - 520)

  J1 = t.Turtle()
  J1.shape(tts)
  J1.pu()
  J1.goto(x2, y2 - 585)

  J2 = t.Turtle()
  J2.shape(tts)
  J2.pu()
  J2.goto(x2 + 65, y2 - 585)

  J3 = t.Turtle()
  J3.shape(tts)
  J3.pu()
  J3.goto(x2 + 130, y2 - 585)

  J4 = t.Turtle()
  J4.shape(tts)
  J4.pu()
  J4.goto(x2 + 195, y2 - 585)

  J5 = t.Turtle()
  J5.shape(tts)
  J5.pu()
  J5.goto(x2 + 260, y2 - 585)

  J6 = t.Turtle()
  J6.shape(tts)
  J6.pu()
  J6.goto(x2 + 325, y2 - 585)

  J7 = t.Turtle()
  J7.shape(tts)
  J7.pu()
  J7.goto(x2 + 390, y2 - 585)

  J8 = t.Turtle()
  J8.shape(tts)
  J8.pu()
  J8.goto(x2 + 455, y2 - 585)

  J9 = t.Turtle()
  J9.shape(tts)
  J9.pu()
  J9.goto(x2 + 520, y2 - 585)

  J10 = t.Turtle()
  J10.shape(tts)
  J10.pu()
  J10.goto(x2 + 585, y2 - 585)


def ship_create(ship_row, ship_column):
  global bd
  # -aircraftCarrier-------------------------------------
  rOu = random.randint(0, 1)
  tempbool = True

  # right or up
  if rOu == 0:
    # up = 0
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column][
          ship_row + 1] != " " and bd[ship_column][
            ship_row + 2] != " " and bd[ship_column][
              ship_row + 3] != " " and bd[ship_column][ship_row + 4] != " ":
        ship_row = random.randint(4, 5)
        ship_column = random.randint(4, 5)
      else:
        for i in range(aircraftCarrier):
          bd[ship_column][ship_row] = "A"
          ship_column += 1
        tempbool = False
  elif rOu == 1:
    # right = 1
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[
          ship_column +
          1][ship_row] != " " and bd[ship_column + 2][ship_row] != " " and bd[
            ship_column + 3][ship_row] != " " and bd[ship_column +
                                                     4][ship_row] != " ":
        ship_row = random.randint(4, 5)
        ship_column = random.randint(4, 5)
      else:
        for i in range(aircraftCarrier):
          bd[ship_column][ship_row] = "A"
          ship_row += 1
        tempbool = False

  # -battleship-------------------------------------
  ship_row = random.randint(3, 6)
  ship_column = random.randint(3, 6)
  rOu = random.randint(0, 1)
  tempbool = True

  # right or up
  if rOu == 0:
    # up = 0
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column][
          ship_row + 1] != " " and bd[ship_column][
            ship_row + 2] != " " and bd[ship_column][ship_row + 3] != " ":
        ship_row = random.randint(3, 6)
        ship_column = random.randint(3, 6)
      else:
        for i in range(battleship):
          bd[ship_column][ship_row] = "B"
          ship_column += 1
        tempbool = False
  elif rOu == 1:
    # right = 1
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[
          ship_column + 1][ship_row] != " " and bd[
            ship_column + 2][ship_row] != " " and bd[ship_column +
                                                     3][ship_row] != " ":
        ship_row = random.randint(3, 6)
        ship_column = random.randint(3, 6)
      else:
        for i in range(battleship):
          bd[ship_column][ship_row] = "B"
          ship_row += 1
        tempbool = False

  # -submarine-------------------------------------
  ship_row = random.randint(2, 7)
  ship_column = random.randint(2, 7)
  rOu = random.randint(0, 1)
  tempbool = True

  # right or up
  if rOu == 0:
    # up = 0
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column][
          ship_row + 1] != " " and bd[ship_column][ship_row + 2] != " ":
        ship_row = random.randint(2, 7)
        ship_column = random.randint(2, 7)
      else:
        for i in range(submarine):
          bd[ship_column][ship_row] = "S"
          ship_column += 1
        tempbool = False
  elif rOu == 1:
    # right = 1
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[
          ship_column + 1][ship_row] != " " and bd[ship_column +
                                                   2][ship_row] != " ":
        ship_row = random.randint(2, 7)
        ship_column = random.randint(2, 7)
      else:
        for i in range(submarine):
          bd[ship_column][ship_row] = "S"
          ship_row += 1
        tempbool = False

    # -cruiser-------------------------------------
  ship_row = random.randint(2, 7)
  ship_column = random.randint(2, 7)
  rOu = random.randint(0, 1)
  tempbool = True

  # right or up
  if rOu == 0:
    # up = 0
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column][
          ship_row + 1] != " " and bd[ship_column][ship_row + 2] != " ":
        ship_row = random.randint(2, 7)
        ship_column = random.randint(2, 7)
      else:
        for i in range(cruiser):
          bd[ship_column][ship_row] = "C"
          ship_column += 1
        tempbool = False
  elif rOu == 1:
    # right = 1
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[
          ship_column + 1][ship_row] != " " and bd[ship_column +
                                                   2][ship_row] != " ":
        ship_row = random.randint(2, 7)
        ship_column = random.randint(2, 7)
      else:
        for i in range(cruiser):
          bd[ship_column][ship_row] = "C"
          ship_row += 1
        tempbool = False
  # -destroyer-------------------------------------
  ship_row = random.randint(1, 8)
  ship_column = random.randint(1, 8)
  rOu = random.randint(0, 1)
  tempbool = True

  # right or up
  if rOu == 0:
    # up = 0
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column][ship_row +
                                                              1] != " ":
        ship_row = random.randint(1, 8)
        ship_column = random.randint(1, 8)
      else:
        for i in range(destroyer):
          bd[ship_column][ship_row] = "D"
          ship_column += 1
        tempbool = False
  elif rOu == 1:
    # right = 1
    while tempbool == True:
      if bd[ship_column][ship_row] != " " and bd[ship_column +
                                                 1][ship_row] != " ":
        ship_row = random.randint(1, 8)
        ship_column = random.randint(1, 8)
      else:
        for i in range(destroyer):
          bd[ship_column][ship_row] = "D"
          ship_row += 1
        tempbool = False

# -----------------------------------------

def set_layout(x, y):
  t.pencolor("lightblue")
  for l in range(11):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.forward(650)
    y -= 65

  for l in range(11):
    t.setheading(0)
    t.pu()
    t.goto(x, 315)
    t.right(90)
    t.pd()
    t.forward(650)
    x += 65

  t.pu()
  t.goto(-320, 325)
  t.pencolor("lightblue")
  t.left(90)
  t.write(" 1 ", font=font_setup)
  t.forward(65)
  t.write(" 2 ", font=font_setup)
  t.forward(65)
  t.write(" 3 ", font=font_setup)
  t.forward(65)
  t.write(" 4 ", font=font_setup)
  t.forward(65)
  t.write(" 5 ", font=font_setup)
  t.forward(65)
  t.write(" 6 ", font=font_setup)
  t.forward(65)
  t.write(" 7 ", font=font_setup)
  t.forward(65)
  t.write(" 8 ", font=font_setup)
  t.forward(65)
  t.write(" 9 ", font=font_setup)
  t.forward(50)
  t.write(" 10 ", font=font_setup)

  t.pu()
  t.goto(-370, 325)
  t.right(90)
  t.forward(65)
  t.write("A", font=font_setup)
  t.forward(65)
  t.write("B", font=font_setup)
  t.forward(65)
  t.write("C", font=font_setup)
  t.forward(65)
  t.write("D", font=font_setup)
  t.forward(65)
  t.write("E", font=font_setup)
  t.forward(65)
  t.write("F", font=font_setup)
  t.forward(65)
  t.write("G", font=font_setup)
  t.forward(65)
  t.write("H", font=font_setup)
  t.forward(65)
  t.write("I", font=font_setup)
  t.forward(65)
  t.write("J", font=font_setup)

set_layout(x, y)
create_spots()
def check_ship_locations():
  global a1
  global a2
  global a3
  global a4
  global a5
  global a6
  global a7
  global a8
  global a9
  global a10
  global b1
  global b2
  global b3
  global b4
  global b5
  global b6
  global b7
  global b8
  global b9
  global b10
  global c1
  global c2
  global c3
  global c4
  global c5
  global c6
  global c7
  global c8
  global c9
  global c10
  global d1
  global d2
  global d3
  global d4
  global d5
  global d6
  global d7
  global d8
  global d9
  global d10
  global e1
  global e2
  global e3
  global e4
  global e5
  global e6
  global e7
  global e8
  global e9
  global e10
  global f1
  global f2
  global f3
  global f4
  global f5
  global f6
  global f7
  global f8
  global f9
  global f10
  global g1
  global g2
  global g3
  global g4
  global g5
  global g6
  global g7
  global g8
  global g9
  global g10
  global h1
  global h2
  global h3
  global h4
  global h5
  global h6
  global h7
  global h8
  global h9
  global h10
  global i1
  global i2
  global i3
  global i4
  global i5
  global i6
  global i7
  global i8
  global i9
  global i10
  global j1
  global j2
  global j3
  global j4
  global j5
  global j6
  global j7
  global j8
  global j9
  global j10
  global tempInt
  global bd

  a1 = False
  a2 = False
  a3 = False
  a4 = False
  a5 = False
  a6 = False
  a7 = False
  a8 = False
  a9 = False
  a10 = False
  b1 = False
  b2 = False
  b3 = False
  b4 = False
  b5 = False
  b6 = False
  b7 = False
  b8 = False
  b9 = False
  b10 = False
  c1 = False
  c2 = False
  c3 = False
  c4 = False
  c5 = False
  c6 = False
  c7 = False
  c8 = False
  c9 = False
  c10 = False
  d1 = False
  d2 = False
  d3 = False
  d4 = False
  d5 = False
  d6 = False
  d7 = False
  d8 = False
  d9 = False
  d10 = False
  e1 = False
  e2 = False
  e3 = False
  e4 = False
  e5 = False
  e6 = False
  e7 = False
  e8 = False
  e9 = False
  e10 = False
  f1 = False
  f2 = False
  f3 = False
  f4 = False
  f5 = False
  f6 = False
  f7 = False
  f8 = False
  f9 = False
  f10 = False
  g1 = False
  g2 = False
  g3 = False
  g4 = False
  g5 = False
  g6 = False
  g7 = False
  g8 = False
  g9 = False
  g10 = False
  h1 = False
  h2 = False
  h3 = False
  h4 = False
  h5 = False
  h6 = False
  h7 = False
  h8 = False
  h9 = False
  h10 = False
  i1 = False
  i2 = False
  i3 = False
  i4 = False
  i5 = False
  i6 = False
  i7 = False
  i8 = False
  i9 = False
  i10 = False
  j1 = False
  j2 = False
  j3 = False
  j4 = False
  j5 = False
  j6 = False
  j7 = False
  j8 = False
  j9 = False
  j10 = False
  
  ship_create(ship_row, ship_column)

  if bd[0][0] != " ":
    a1 = True
    tempInt +=1
  if bd[0][1] != " ":
    a2 = True
    tempInt +=1
  if bd[0][2] != " ":
    a3 = True
    tempInt +=1
  if bd[0][3] != " ":
    a4 = True
    tempInt +=1
  if bd[0][4] != " ":
    a5 = True
    tempInt +=1
  if bd[0][5] != " ":
    a6 = True
    tempInt +=1
  if bd[0][6] != " ":
    a7 = True
    tempInt +=1
  if bd[0][7] != " ":
    a8 = True
    tempInt +=1
  if bd[0][8] != " ":
    a9 = True
    tempInt +=1
  if bd[0][9] != " ":
    a10 = True
    tempInt +=1
  if bd[1][0] != " ":
    b1 = True
    tempInt +=1
  if bd[1][1] != " ":
    b2 = True
    tempInt +=1
  if bd[1][2] != " ":
    b3 = True
    tempInt +=1
  if bd[1][3] != " ":
    b4 = True
    tempInt +=1
  if bd[1][4] != " ":
    b5 = True
    tempInt +=1
  if bd[1][5] != " ":
    b6 = True
    tempInt +=1
  if bd[1][6] != " ":
    b7 = True
    tempInt +=1
  if bd[1][7] != " ":
    b8 = True
    tempInt +=1
  if bd[1][8] != " ":
    b9 = True
    tempInt +=1
  if bd[1][9] != " ":
    b10 = True
    tempInt +=1
  if bd[2][0] != " ":
    c1 = True
    tempInt +=1
  if bd[2][1] != " ":
    c2 = True
    tempInt +=1
  if bd[2][2] != " ":
    c3 = True
    tempInt +=1
  if bd[2][3] != " ":
    c4 = True
    tempInt +=1
  if bd[2][4] != " ":
    c5 = True
    tempInt +=1
  if bd[2][5] != " ":
    c6 = True
    tempInt +=1
  if bd[2][6] != " ":
    c7 = True
    tempInt +=1
  if bd[2][7] != " ":
    c8 = True
    tempInt +=1
  if bd[2][8] != " ":
    c9 = True
    tempInt +=1
  if bd[2][9] != " ":
    c10 = True
    tempInt +=1
  if bd[3][0] != " ":
    d1 = True
    tempInt +=1
  if bd[3][1] != " ":
    d2 = True
    tempInt +=1
  if bd[3][2] != " ":
    d3 = True
    tempInt +=1
  if bd[3][3] != " ":
    d4 = True
    tempInt +=1
  if bd[3][4] != " ":
    d5 = True
    tempInt +=1
  if bd[3][5] != " ":
    d6 = True
    tempInt +=1
  if bd[3][6] != " ":
    d7 = True
    tempInt +=1
  if bd[3][7] != " ":
    d8 = True
    tempInt +=1
  if bd[3][8] != " ":
    d9 = True
    tempInt +=1
  if bd[3][9] != " ":
    d10 = True
    tempInt +=1
  if bd[4][0] != " ":
    e1 = True
    tempInt +=1
  if bd[4][1] != " ":
    e2 = True
    tempInt +=1
  if bd[4][2] != " ":
    e3 = True
    tempInt +=1
  if bd[4][3] != " ":
    e4 = True
    tempInt +=1
  if bd[4][4] != " ":
    e5 = True
    tempInt +=1
  if bd[4][5] != " ":
    e6 = True
    tempInt +=1
  if bd[4][6] != " ":
    e7 = True
    tempInt +=1
  if bd[4][7] != " ":
    e8 = True
    tempInt +=1
  if bd[4][8] != " ":
    e9 = True
    tempInt +=1
  if bd[4][9] != " ":
    e10 = True
    tempInt +=1
  if bd[5][0] != " ":
    f1 = True
    tempInt +=1
  if bd[5][1] != " ":
    f2 = True
    tempInt +=1
  if bd[5][2] != " ":
    f3 = True
    tempInt +=1
  if bd[5][3] != " ":
    f4 = True
    tempInt +=1
  if bd[5][4] != " ":
    f5 = True
    tempInt +=1
  if bd[5][5] != " ":
    f6 = True
    tempInt +=1
  if bd[5][6] != " ":
    f7 = True
    tempInt +=1
  if bd[5][7] != " ":
    f8 = True
    tempInt +=1
  if bd[5][8] != " ":
    f9 = True
    tempInt +=1
  if bd[5][9] != " ":
    f10 = True
    tempInt +=1
  if bd[6][0] != " ":
    g1 = True
    tempInt +=1
  if bd[6][1] != " ":
    g2 = True
    tempInt +=1
  if bd[6][2] != " ":
    g3 = True
    tempInt +=1
  if bd[6][3] != " ":
    g4 = True
    tempInt +=1
  if bd[6][4] != " ":
    g5 = True
    tempInt +=1
  if bd[6][5] != " ":
    g6 = True
    tempInt +=1
  if bd[6][6] != " ":
    g7 = True
    tempInt +=1
  if bd[6][7] != " ":
    g8 = True
    tempInt +=1
  if bd[6][8] != " ":
    g9 = True
    tempInt +=1
  if bd[6][9] != " ":
    g10 = True
    tempInt +=1
  if bd[7][0] != " ":
    h1 = True
    tempInt +=1
  if bd[7][1] != " ":
    h2 = True
    tempInt +=1
  if bd[7][2] != " ":
    h3 = True
    tempInt +=1
  if bd[7][3] != " ":
    h4 = True
    tempInt +=1
  if bd[7][4] != " ":
    h5 = True
    tempInt +=1
  if bd[7][5] != " ":
    h6 = True
    tempInt +=1
  if bd[7][6] != " ":
    h7 = True
    tempInt +=1
  if bd[7][7] != " ":
    h8 = True
    tempInt +=1
  if bd[7][8] != " ":
    h9 = True
    tempInt +=1
  if bd[7][9] != " ":
    h10 = True
    tempInt +=1
  if bd[8][0] != " ":
    i1 = True
    tempInt +=1
  if bd[8][1] != " ":
    i2 = True
    tempInt +=1
  if bd[8][2] != " ":
    i3 = True
    tempInt +=1
  if bd[8][3] != " ":
    i4 = True
    tempInt +=1
  if bd[8][4] != " ":
    i5 = True
    tempInt +=1
  if bd[8][5] != " ":
    i6 = True
    tempInt +=1
  if bd[8][6] != " ":
    i7 = True
    tempInt +=1
  if bd[8][7] != " ":
    i8 = True
    tempInt +=1
  if bd[8][8] != " ":
    i9 = True
    tempInt +=1
  if bd[8][9] != " ":
    i10 = True
    tempInt +=1
  if bd[9][0] != " ":
    j1 = True
    tempInt +=1
  if bd[9][1] != " ":
    j2 = True
    tempInt +=1
  if bd[9][2] != " ":
    j3 = True
    tempInt +=1
  if bd[9][3] != " ":
    j4 = True
    tempInt +=1
  if bd[9][4] != " ":
    j5 = True
    tempInt +=1
  if bd[9][5] != " ":
    j6 = True
    tempInt +=1
  if bd[9][6] != " ":
    j7 = True
    tempInt +=1
  if bd[9][7] != " ":
    j8 = True
    tempInt +=1
  if bd[9][8] != " ":
    j9 = True
    tempInt +=1
  if bd[9][9] != " ":
    j10 = True
    tempInt +=1

  while tempInt != 17:
    tempInt = 0
    bd = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    check_ship_locations()

check_ship_locations()
t.update()

# print("  1    2    3    4    5    6    7    8    9    10")
# for i in range(len(bd)):
#   print(bd[i])

t.tracer(True)

def place_a1(x, y):
  global turns
  global ship_spots_left
  if a1:
    A1.shape(hit)
    ship_spots_left -= 1
    turns -= 1
    update_turnsleft()
  if not a1:
    A1.shape(miss)
    update_turnsleft()
  A1.stamp()
  A1.hideturtle()
def place_a2(x, y):
  if a2:
    A2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a2:
    A2.shape(miss)
    update_turnsleft()
  A2.stamp()
  A2.hideturtle()
def place_a3(x, y):
  if a3:
    A3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a3:
    A3.shape(miss)
    update_turnsleft()
  A3.stamp()
  A3.hideturtle()
def place_a4(x, y):
  if a4:
    A4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a4:
    A4.shape(miss)
    update_turnsleft()
  A4.stamp()
  A4.hideturtle()
def place_a5(x, y):
  if a5:
    A5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a5:
    A5.shape(miss)
    update_turnsleft()
  A5.stamp()
  A5.hideturtle()
def place_a6(x, y):
  if a6:
    A6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a6:
    A6.shape(miss)
    update_turnsleft()
  A6.stamp()
  A6.hideturtle()
def place_a7(x, y):
  if a7:
    A7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a7:
    A7.shape(miss)
    update_turnsleft()
  A7.stamp()
  A7.hideturtle()
def place_a8(x, y):
  if a8:
    A8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a8:
    A8.shape(miss)
    update_turnsleft()
  A8.stamp()
  A8.hideturtle()
def place_a9(x, y):
  if a9:
    A9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a9:
    A9.shape(miss)
    update_turnsleft()
  A9.stamp()
  A9.hideturtle()
def place_a10(x, y):
  if a10:
    A10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not a10:
    A10.shape(miss)
    update_turnsleft()
  A10.stamp()
  A10.hideturtle()
def place_b1(x, y):
  if b1:
    B1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b1:
    B1.shape(miss)
    update_turnsleft()
  B1.stamp()
  B1.hideturtle()
def place_b2(x, y):
  if b2:
    B2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b2:
    B2.shape(miss)
    update_turnsleft()
  B2.stamp()
  B2.hideturtle()
def place_b3(x, y):
  if b3:
    B3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b3:
    B3.shape(miss)
    update_turnsleft()
  B3.stamp()
  B3.hideturtle()
def place_b4(x, y):
  if b4:
    B4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b4:
    B4.shape(miss)
    update_turnsleft()
  B4.stamp()
  B4.hideturtle()
def place_b5(x, y):
  if b5:
    B5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b5:
    B5.shape(miss)
    update_turnsleft()
  B5.stamp()
  B5.hideturtle()
def place_b6(x, y):
  if b6:
    B6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b6:
    B6.shape(miss)
    update_turnsleft()
  B6.stamp()
  B6.hideturtle()
def place_b7(x, y):
  if b7:
    B7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b7:
    B7.shape(miss)
    update_turnsleft()
  B7.stamp()
  B7.hideturtle()
def place_b8(x, y):
  if b8:
    B8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b8:
    B8.shape(miss)
    update_turnsleft()
  B8.stamp()
  B8.hideturtle()
def place_b9(x, y):
  if b9:
    B9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b9:
    B9.shape(miss)
    update_turnsleft()
  B9.stamp()
  B9.hideturtle()
def place_b10(x, y):
  if b10:
    B10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not b10:
    B10.shape(miss)
    update_turnsleft()
  B10.stamp()
  B10.hideturtle()
def place_c1(x, y):
  if c1:
    C1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c1:
    C1.shape(miss)
    update_turnsleft()
  C1.stamp()
  C1.hideturtle()
def place_c2(x, y):
  if c2:
    C2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c2:
    C2.shape(miss)
    update_turnsleft()
  C2.stamp()
  C2.hideturtle()
def place_c3(x, y):
  if c3:
    C3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c3:
    C3.shape(miss)
    update_turnsleft()
  C3.stamp()
  C3.hideturtle()
def place_c4(x, y):
  if c4:
    C4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c4:
    C4.shape(miss)
    update_turnsleft()
  C4.stamp()
  C4.hideturtle()
def place_c5(x, y):
  if c5:
    C5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c5:
    C5.shape(miss)
    update_turnsleft()
  C5.stamp()
  C5.hideturtle()
def place_c6(x, y):
  if c6:
    C6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c6:
    C6.shape(miss)
    update_turnsleft()
  C6.stamp()
  C6.hideturtle()
def place_c7(x, y):
  if c7:
    C7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c7:
    C7.shape(miss)
    update_turnsleft()
  C7.stamp()
  C7.hideturtle()
def place_c8(x, y):
  if c8:
    C8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c8:
    C8.shape(miss)
    update_turnsleft()
  C8.stamp()
  C8.hideturtle()
def place_c9(x, y):
  if c9:
    C9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c9:
    C9.shape(miss)
    update_turnsleft()
  C9.stamp()
  C9.hideturtle()
def place_c10(x, y):
  if c10:
    C10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not c10:
    C10.shape(miss)
    update_turnsleft()
  C10.stamp()
  C10.hideturtle()
def place_d1(x, y):
  if d1:
    D1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d1:
    D1.shape(miss)
    update_turnsleft()
  D1.stamp()
  D1.hideturtle()
def place_d2(x, y):
  if d2:
    D2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d2:
    D2.shape(miss)
    update_turnsleft()
  D2.stamp()
  D2.hideturtle()
def place_d3(x, y):
  if d3:
    D3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d3:
    D3.shape(miss)
    update_turnsleft()
  D3.stamp()
  D3.hideturtle()
def place_d4(x, y):
  if d4:
    D4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d4:
    D4.shape(miss)
    update_turnsleft()
  D4.stamp()
  D4.hideturtle()
def place_d5(x, y):
  if d5:
    D5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d5:
    D5.shape(miss)
    update_turnsleft()
  D5.stamp()
  D5.hideturtle()
def place_d6(x, y):
  if d6:
    D6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d6:
    D6.shape(miss)
    update_turnsleft()
  D6.stamp()
  D6.hideturtle()
def place_d7(x, y):
  if d7:
    D7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d7:
    D7.shape(miss)
    update_turnsleft()
  D7.stamp()
  D7.hideturtle()
def place_d8(x, y):
  if d8:
    D8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d8:
    D8.shape(miss)
    update_turnsleft()
  D8.stamp()
  D8.hideturtle()
def place_d9(x, y):
  if d9:
    D9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d9:
    D9.shape(miss)
    update_turnsleft()
  D9.stamp()
  D9.hideturtle()
def place_d10(x, y):
  if d10:
    D10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not d10:
    D10.shape(miss)
    update_turnsleft()
  D10.stamp()
  D10.hideturtle()
def place_e1(x, y):
  if e1:
    E1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e1:
    E1.shape(miss)
    update_turnsleft()
  E1.stamp()
  E1.hideturtle()
def place_e2(x, y):
  if e2:
    E2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e2:
    E2.shape(miss)
    update_turnsleft()
  E2.stamp()
  E2.hideturtle()
def place_e3(x, y):
  if e3:
    E3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e3:
    E3.shape(miss)
    update_turnsleft()
  E3.stamp()
  E3.hideturtle()
def place_e4(x, y):
  if e4:
    E4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e4:
    E4.shape(miss)
    update_turnsleft()
  E4.stamp()
  E4.hideturtle()
def place_e5(x, y):
  if e5:
    E5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e5:
    E5.shape(miss)
    update_turnsleft()
  E5.stamp()
  E5.hideturtle()
def place_e6(x, y):
  if e6:
    E6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e6:
    E6.shape(miss)
    update_turnsleft()
  E6.stamp()
  E6.hideturtle()
def place_e7(x, y):
  if e7:
    E7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e7:
    E7.shape(miss)
    update_turnsleft()
  E7.stamp()
  E7.hideturtle()
def place_e8(x, y):
  if e8:
    E8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e8:
    E8.shape(miss)
    update_turnsleft()
  E8.stamp()
  E8.hideturtle()
def place_e9(x, y):
  if e9:
    E9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e9:
    E9.shape(miss)
    update_turnsleft()
  E9.stamp()
  E9.hideturtle()
def place_e10(x, y):
  if e10:
    E10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not e10:
    E10.shape(miss)
    update_turnsleft()
  E10.stamp()
  E10.hideturtle()
def place_f1(x, y):
  if f1:
    F1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f1:
    F1.shape(miss)
    update_turnsleft()
  F1.stamp()
  F1.hideturtle()
def place_f2(x, y):
  if f2:
    F2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f2:
    F2.shape(miss)
    update_turnsleft()
  F2.stamp()
  F2.hideturtle()
def place_f3(x, y):
  if f3:
    F3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f3:
    F3.shape(miss)
    update_turnsleft()
  F3.stamp()
  F3.hideturtle()
def place_f4(x, y):
  if f4:
    F4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f4:
    F4.shape(miss)
    update_turnsleft()
  F4.stamp()
  F4.hideturtle()
def place_f5(x, y):
  if f5:
    F5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f5:
    F5.shape(miss)
    update_turnsleft()
  F5.stamp()
  F5.hideturtle()
def place_f6(x, y):
  if f6:
    F6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f6:
    F6.shape(miss)
    update_turnsleft()
  F6.stamp()
  F6.hideturtle()
def place_f7(x, y):
  if f7:
    F7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f7:
    F7.shape(miss)
    update_turnsleft()
  F7.stamp()
  F7.hideturtle()
def place_f8(x, y):
  if f8:
    F8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f8:
    F8.shape(miss)
    update_turnsleft()
  F8.stamp()
  F8.hideturtle()
def place_f9(x, y):
  if f9:
    F9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f9:
    F9.shape(miss)
    update_turnsleft()
  F9.stamp()
  F9.hideturtle()
def place_f10(x, y):
  if f10:
    F10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not f10:
    F10.shape(miss)
    update_turnsleft()
  F10.stamp()
  F10.hideturtle()
def place_g1(x, y):
  if g1:
    G1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g1:
    G1.shape(miss)
    update_turnsleft()
  G1.stamp()
  G1.hideturtle()
def place_g2(x, y):
  if g2:
    G2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g2:
    G2.shape(miss)
    update_turnsleft()
  G2.stamp()
  G2.hideturtle()
def place_g3(x, y):
  if g3:
    G3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g3:
    G3.shape(miss)
    update_turnsleft()
  G3.stamp()
  G3.hideturtle()
def place_g4(x, y):
  if g4:
    G4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g4:
    G4.shape(miss)
    update_turnsleft()
  G4.stamp()
  G4.hideturtle()
def place_g5(x, y):
  if g5:
    G5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g5:
    G5.shape(miss)
    update_turnsleft()
  G5.stamp()
  G5.hideturtle()
def place_g6(x, y):
  if g6:
    G6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g6:
    G6.shape(miss)
    update_turnsleft()
  G6.stamp()
  G6.hideturtle()
def place_g7(x, y):
  if g7:
    G7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g7:
    G7.shape(miss)
    update_turnsleft()
  G7.stamp()
  G7.hideturtle()
def place_g8(x, y):
  if g8:
    G8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g8:
    G8.shape(miss)
    update_turnsleft()
  G8.stamp()
  G8.hideturtle()
def place_g9(x, y):
  if g9:
    G9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g9:
    G9.shape(miss)
    update_turnsleft()
  G9.stamp()
  G9.hideturtle()
def place_g10(x, y):
  if g10:
    G10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not g10:
    G10.shape(miss)
    update_turnsleft()
  G10.stamp()
  G10.hideturtle()
def place_h1(x, y):
  if h1:
    H1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h1:
    H1.shape(miss)
    update_turnsleft()
  H1.stamp()
  H1.hideturtle()
def place_h2(x, y):
  if h2:
    H2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h2:
    H2.shape(miss)
    update_turnsleft()
  H2.stamp()
  H2.hideturtle()
def place_h3(x, y):
  if h3:
    H3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h3:
    H3.shape(miss)
    update_turnsleft()
  H3.stamp()
  H3.hideturtle()
def place_h4(x, y):
  if h4:
    H4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h4:
    H4.shape(miss)
    update_turnsleft()
  H4.stamp()
  H4.hideturtle()
def place_h5(x, y):
  if h5:
    H5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h5:
    H5.shape(miss)
    update_turnsleft()
  H5.stamp()
  H5.hideturtle()
def place_h6(x, y):
  if h6:
    H6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h6:
    H6.shape(miss)
    update_turnsleft()
  H6.stamp()
  H6.hideturtle()
def place_h7(x, y):
  if h7:
    H7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h7:
    H7.shape(miss)
    update_turnsleft()
  H7.stamp()
  H7.hideturtle()
def place_h8(x, y):
  if h8:
    H8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h8:
    H8.shape(miss)
    update_turnsleft()
  H8.stamp()
  H8.hideturtle()
def place_h9(x, y):
  if h9:
    H9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h9:
    H9.shape(miss)
    update_turnsleft()
  H9.stamp()
  H9.hideturtle()
def place_h10(x, y):
  if h10:
    H10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not h10:
    H10.shape(miss)
    update_turnsleft()
  H10.stamp()
  H10.hideturtle()
def place_i1(x, y):
  if i1:
    I1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i1:
    I1.shape(miss)
    update_turnsleft()
  I1.stamp()
  I1.hideturtle()
def place_i2(x, y):
  if i2:
    I2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i2:
    I2.shape(miss)
    update_turnsleft()
  I2.stamp()
  I2.hideturtle()
def place_i3(x, y):
  if i3:
    I3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i3:
    I3.shape(miss)
    update_turnsleft()
  I3.stamp()
  I3.hideturtle()
def place_i4(x, y):
  if i4:
    I4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i4:
    I4.shape(miss)
    update_turnsleft()
  I4.stamp()
  I4.hideturtle()
def place_i5(x, y):
  if i5:
    I5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i5:
    I5.shape(miss)
    update_turnsleft()
  I5.stamp()
  I5.hideturtle()
def place_i6(x, y):
  if i6:
    I6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i6:
    I6.shape(miss)
    update_turnsleft()
  I6.stamp()
  I6.hideturtle()
def place_i7(x, y):
  if i7:
    I7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i7:
    I7.shape(miss)
    update_turnsleft()
  I7.stamp()
  I7.hideturtle()
def place_i8(x, y):
  if i8:
    I8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i8:
    I8.shape(miss)
    update_turnsleft()
  I8.stamp()
  I8.hideturtle()
def place_i9(x, y):
  if i9:
    I9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i9:
    I9.shape(miss)
    update_turnsleft()
  I9.stamp()
  I9.hideturtle()
def place_i10(x, y):
  if i10:
    I10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not i10:
    I10.shape(miss)
    update_turnsleft()
  I10.stamp()
  I10.hideturtle()
def place_j1(x, y):
  if j1:
    J1.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j1:
    J1.shape(miss)
    update_turnsleft()
  J1.stamp()
  J1.hideturtle()
def place_j2(x, y):
  if j2:
    J2.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j2:
    J2.shape(miss)
    update_turnsleft()
  J2.stamp()
  J2.hideturtle()
def place_j3(x, y):
  if j3:
    J3.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j3:
    J3.shape(miss)
    update_turnsleft()
  J3.stamp()
  J3.hideturtle()
def place_j4(x, y):
  if j4:
    J4.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j4:
    J4.shape(miss)
    update_turnsleft()
  J4.stamp()
  J4.hideturtle()
def place_j5(x, y):
  if j5:
    J5.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j5:
    J5.shape(miss)
    update_turnsleft()
  J5.stamp()
  J5.hideturtle()
def place_j6(x, y):
  if j6:
    J6.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j6:
    J6.shape(miss)
    update_turnsleft()
  J6.stamp()
  J6.hideturtle()
def place_j7(x, y):
  if j7:
    J7.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j7:
    J7.shape(miss)
    update_turnsleft()
  J7.stamp()
  J7.hideturtle()
def place_j8(x, y):
  if j8:
    J8.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j8:
    J8.shape(miss)
    update_turnsleft()
  J8.stamp()
  J8.hideturtle()
def place_j9(x, y):
  if j9:
    J9.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j9:
    J9.shape(miss)
    update_turnsleft()
  J9.stamp()
  J9.hideturtle()
def place_j10(x, y):
  if j10:
    J10.shape(hit)
    global ship_spots_left
    ship_spots_left -= 1
    update_turnsleft()
  if not j10:
    J10.shape(miss)
    update_turnsleft()
  J10.stamp()
  J10.hideturtle()

A1.onclick(place_a1)
A2.onclick(place_a2)
A3.onclick(place_a3)
A4.onclick(place_a4)
A5.onclick(place_a5)
A6.onclick(place_a6)
A7.onclick(place_a7)
A8.onclick(place_a8)
A9.onclick(place_a9)
A10.onclick(place_a10)
B1.onclick(place_b1)
B2.onclick(place_b2)
B3.onclick(place_b3)
B4.onclick(place_b4)
B5.onclick(place_b5)
B6.onclick(place_b6)
B7.onclick(place_b7)
B8.onclick(place_b8)
B9.onclick(place_b9)
B10.onclick(place_b10)
C1.onclick(place_c1)
C2.onclick(place_c2)
C3.onclick(place_c3)
C4.onclick(place_c4)
C5.onclick(place_c5)
C6.onclick(place_c6)
C7.onclick(place_c7)
C8.onclick(place_c8)
C9.onclick(place_c9)
C10.onclick(place_c10)
D1.onclick(place_d1)
D2.onclick(place_d2)
D3.onclick(place_d3)
D4.onclick(place_d4)
D5.onclick(place_d5)
D6.onclick(place_d6)
D7.onclick(place_d7)
D8.onclick(place_d8)
D9.onclick(place_d9)
D10.onclick(place_d10)
E1.onclick(place_e1)
E2.onclick(place_e2)
E3.onclick(place_e3)
E4.onclick(place_e4)
E5.onclick(place_e5)
E6.onclick(place_e6)
E7.onclick(place_e7)
E8.onclick(place_e8)
E9.onclick(place_e9)
E10.onclick(place_e10)
F1.onclick(place_f1)
F2.onclick(place_f2)
F3.onclick(place_f3)
F4.onclick(place_f4)
F5.onclick(place_f5)
F6.onclick(place_f6)
F7.onclick(place_f7)
F8.onclick(place_f8)
F9.onclick(place_f9)
F10.onclick(place_f10)
G1.onclick(place_g1)
G2.onclick(place_g2)
G3.onclick(place_g3)
G4.onclick(place_g4)
G5.onclick(place_g5)
G6.onclick(place_g6)
G7.onclick(place_g7)
G8.onclick(place_g8)
G9.onclick(place_g9)
G10.onclick(place_g10)
H1.onclick(place_h1)
H2.onclick(place_h2)
H3.onclick(place_h3)
H4.onclick(place_h4)
H5.onclick(place_h5)
H6.onclick(place_h6)
H7.onclick(place_h7)
H8.onclick(place_h8)
H9.onclick(place_h9)
H10.onclick(place_h10)
I1.onclick(place_i1)
I2.onclick(place_i2)
I3.onclick(place_i3)
I4.onclick(place_i4)
I5.onclick(place_i5)
I6.onclick(place_i6)
I7.onclick(place_i7)
I8.onclick(place_i8)
I9.onclick(place_i9)
I10.onclick(place_i10)
J1.onclick(place_j1)
J2.onclick(place_j2)
J3.onclick(place_j3)
J4.onclick(place_j4)
J5.onclick(place_j5)
J6.onclick(place_j6)
J7.onclick(place_j7)
J8.onclick(place_j8)
J9.onclick(place_j9)
J10.onclick(place_j10)
    
wn.mainloop()