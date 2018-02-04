import turtle
end = 0
wn = turtle.Screen()
table_loop = 0
color_var = 0
square_name = "square"
bsquare_number = 0
wsquare_number = 0
bsquares = []
wsquares = []
piece_loop = 0
pcolor_var = 0
color = "b"
ptype = "pawn"
piece_number = 1
piece_mod = 1
bpieces = []
wpieces = []
imwpieces = []
imbpieces = []
impieces = []
ltmd = 0
xcor = -200
ycor = -200
corvar = 0
tnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
wevalpieces = []
nicewloop = 0
nicebloop = 0
pcrindex = 0
nicesquareloop = 0
picnum = 0
niceimgloop = 0
screen = turtle.Screen()


screen.addshape("selecter.gif")
selecter = turtle.Turtle()
selecter.penup()
selecter.speed(10000)
selecter.setpos(25, 25)
selecter.shape("selecter.gif")
selecter.shapesize(1, 1, 1)



# create board and piece names
while piece_loop != 32:
    if pcolor_var == 16:
        color = "w"
        piece_mod = 1
    if piece_mod == 1:
        ptype = "pawn1"
    if piece_mod == 2:
        ptype = "pawn2"
    if piece_mod == 3:
        ptype = "pawn3"
    if piece_mod == 4:
        ptype = "pawn4"
    if piece_mod == 5:
        ptype = "pawn5"
    if piece_mod == 6:
        ptype = "pawn6"
    if piece_mod == 7:
        ptype = "pawn7"
    if piece_mod == 8:
        ptype = "pawn8"
    if piece_mod == 9:
        ptype = "knight1"
    if piece_mod == 10:
        ptype = "knight2"
    if piece_mod == 11:
        ptype = "bishop1"
    if piece_mod == 12:
        ptype = "bishop2"
    if piece_mod == 13:
        ptype = "rook1"
    if piece_mod == 14:
        ptype = "rook2"
    if piece_mod == 15:
        ptype = "queen"
    if piece_mod == 16:
        ptype = "king"
    piece_name = color + ptype
    if color == "w":
        wpieces.append(piece_name)
    else:
        bpieces.append(piece_name)
    pcolor_var = pcolor_var + 1
    piece_loop = piece_loop + 1
    piece_mod = piece_mod + 1


# create board
screen.bgpic("board.gif")


# create not real board
while nicewloop == 0:
    imwpawn1 = {"xcor": -175, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn1)
    imwpawn2 = {"xcor": -125, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn2)
    imwpawn3 = {"xcor": -75, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn3)
    imwpawn4 = {"xcor": -25, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn4)
    imwpawn5 = {"xcor": 25, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn5)
    imwpawn6 = {"xcor": 75, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn6)
    imwpawn7 = {"xcor": 125, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn7)
    imwpawn8 = {"xcor": 175, "ycor": -125, "moved": False, "typ": "pawn"}
    imwpieces.append(imwpawn8)
    imwknight1 = {"xcor": -125, "ycor": -175, "typ": "knight"}
    imwpieces.append(imwknight1)
    imwknight2 = {"xcor": 125, "ycor": -175, "typ": "knight"}
    imwpieces.append(imwknight2)
    imwbishop1 = {"xcor": -75, "ycor": -175, "typ": "bishop"}
    imwpieces.append(imwbishop1)
    imwbishop2 = {"xcor": 75, "ycor": -175, "typ": "bishop"}
    imwpieces.append(imwbishop2)
    imwqueen = {"xcor": -25, "ycor": -175, "typ": "queen"}
    imwpieces.append(imwqueen)
    imwrook1 = {"xcor": -175, "ycor": -175, "rochet": True, "typ": "rook"}
    imwpieces.append(imwrook1)
    imwrook2 = {"xcor": 175, "ycor": -175, "rochet": True, "typ": "rook"}
    imwpieces.append(imwrook2)
    imwking = {"xcor": 25, "ycor": -175, "rochet": True, "typ": "king"}
    imwpieces.append(imwking)
    nicewloop += 1
while nicebloop == 0:
    imbpawn1 = {"xcor": -175, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn1)
    imbpawn2 = {"xcor": -125, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn2)
    imbpawn3 = {"xcor": -75, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn3)
    imbpawn4 = {"xcor": -25, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn4)
    imbpawn5 = {"xcor": 25, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn5)
    imbpawn6 = {"xcor": 75, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn6)
    imbpawn7 = {"xcor": 125, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn7)
    imbpawn8 = {"xcor": 175, "ycor": 125, "moved": False, "typ": "pawn"}
    imbpieces.append(imbpawn8)
    imbknight1 = {"xcor": -125, "ycor": 175, "typ": "knight"}
    imbpieces.append(imbknight1)
    imbknight2 = {"xcor": 125, "ycor": 175, "typ": "knight"}
    imbpieces.append(imbknight2)
    imbbishop1 = {"xcor": -75, "ycor": 175, "typ": "bishop"}
    imbpieces.append(imbbishop1)
    imbbishop2 = {"xcor": 75, "ycor": 175, "typ": "bishop"}
    imbpieces.append(imbbishop2)
    imbqueen = {"xcor": -25, "ycor": 175, "typ": "queen"}
    imbpieces.append(imbqueen)
    imbrook1 = {"xcor": -175, "ycor": 175, "rochet": True, "typ": "rook"}
    imbpieces.append(imbrook1)
    imbrook2 = {"xcor": 175, "ycor": 175, "rochet": True, "typ": "rook"}
    imbpieces.append(imbrook2)
    imbking = {"xcor": 25, "ycor": 175, "rochet": True, "typ": "king"}
    imbpieces.append(imbking)
    nicebloop += 1
for piece in imwpieces:
    impieces.append(piece)
for piece in imbpieces:
    impieces.append(piece)

# create pieces in visal board
for piece in imbpieces:
    if "pawn" == piece["typ"]:
        ycor = piece["ycor"]
        xcor = piece["xcor"]
    else:
        if "bishop" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "rook" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "knight" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "queen" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "king" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
    bpieces[pcrindex] = turtle.Turtle()
    bpieces[pcrindex].penup()
    bpieces[pcrindex].speed(10000)
    bpieces[pcrindex].color("orange")
    bpieces[pcrindex].setpos(xcor, ycor)
    bpieces[pcrindex].speed(10)
    if pcrindex < len(bpieces)-1:
        pcrindex += 1
pcrindex = 0
for piece in imwpieces:
    if "pawn" == piece["typ"]:
        ycor = piece["ycor"]
        xcor = piece["xcor"]
    else:
        if "bishop" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "rook" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "knight" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "queen" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
        if "king" == piece["typ"]:
            ycor = piece["ycor"]
            xcor = piece["xcor"]
    wpieces[pcrindex] = turtle.Turtle()
    wpieces[pcrindex].penup()
    wpieces[pcrindex].speed(10000)
    wpieces[pcrindex].color("blue")
    wpieces[pcrindex].setpos(xcor, ycor)
    wpieces[pcrindex].speed(10)
    if pcrindex < len(wpieces)-1:
        pcrindex += 1

# create useful functions
def squarecheck(x, y, bsquares, wsquares):
    for sq in bsquares:
        if sq.xcor == x and sq.ycor == y:
            sq.color("green")
    for sq in wsquares:
        if sq.xcor == x and sq.ycor == y:
            sq.color("green")
def checkCheck(x, y, color):
    if color == "white":
        ncolor = "black"
    else:
        ncolor = "white"
    if x and y in  kingStep(x, y, ncolor, False) or queenStep(x, y, ncolor) or rookStep(x, y, ncolor) or knightStep(x, y, ncolor) or bishopStep(x, y, ncolor) or pawnHit(x, y, ncolor):
        return True
    else:
        return False
def checkMateCheck(x, y, color, rochet):
    if kingStep(x, y, color, rochet) == [] and checkCheck(x, y, color, rochet):
        return True
    else:
        return False
def remove_outside_board(places):
    for i in places:
        if i < -200 or i > 150:
            places.remove(i)
    return places


def pawnHit(x, y, color):
    places = []
    if color == "white":
        for piece in imbpieces:
            if piece[x] == x+50 and piece[y] == y+50:
                places.append(x+50)
                places.append(y+50)
            if piece[x] == x-50 and piece[y] == y+50:
                places.append(x-50)
                places.append(y+50)
    if color == "black":
        for piece in imwpieces:
            if piece[x] == x+50 and piece[y] == y-50:
                places.append(x+50)
                places.append(y+50)
            if piece[x] == x-50 and piece[y] == y-50:
                places.append(x-50)
                places.append(y+50)
    return places
def pawnStep(x, y, color, moved):
    places = []
    if color == "white":
        places.append(x - 50)
        places.append(y)
        if not moved:
            places.append(x - 100)
            places.append(y)
    else:
        places.append(x + 50)
        places.append(y)
        if not moved:
            places.append(x + 100)
            places.append(y)
    if color == "white":
        for piece in imbpieces:
            if piece["xcor"] == x + 50:
                if piece["ycor"] == y + 50:
                    places.append(x + 50)
                    places.append(y + 50)
    else:
        for piece in imwpieces:
            if piece["xcor"] == x + 50:
                if piece["ycor"] == y + 50:
                    places.append(x + 50)
                    places.append(y + 50)
    return places
def knightStep(x, y, color):
    places = []
    eval = False
    if color == "white":
        for piece in imwpieces:
            if not (piece["xcor"] == x + 100 and piece["ycor"] == y + 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 100 and piece["ycor"] == y - 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 100 and piece["ycor"] == y + 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 100 and piece["ycor"] == y - 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 50 and piece["ycor"] == y + 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 50 and piece["ycor"] == y - 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 50 and piece["ycor"] == y + 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 50 and piece["ycor"] == y - 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
    else:
        for piece in imbpieces:
            if not (piece["xcor"] == x + 100 and piece["ycor"] == y + 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 100 and piece["ycor"] == y - 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 100 and piece["ycor"] == y + 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 100 and piece["ycor"] == y - 50):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 50 and piece["ycor"] == y + 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x + 50 and piece["ycor"] == y - 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 50 and piece["ycor"] == y + 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
            if not (piece["xcor"] == x - 50 and piece["ycor"] == y - 100):
                eval = True
            if eval == True:
                places.append(x)
                places.append(y)
    return places
def bishopStep(x, y, color):
    blocked = False
    ory = y
    orx = x
    places = []
    if color == "white":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y += 50
        blocked = False
        x = orx
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y -= 50
        blocked = False
        x = ory
        y = ory
    if color == "black":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y += 50
        blocked = False
        x = orx
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y -= 50
        blocked = False
        x = orx
        y = ory
    return places
def rookStep(x, y, color):
    blocked = False
    ory = y
    orx = x
    places = []
    if color == "white":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x += 50
        blocked = False
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
        blocked = False
        x = ory
    if color == "black":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x += 50
        blocked = False
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
        blocked = False
        x = orx
    return places
def queenStep(x, y, color):
    blocked = False
    ory = y
    orx = x
    places = []
    if color == "white":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y += 50
        blocked = False
        x = orx
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y -= 50
        blocked = False
        x = ory
        y = ory
    if color == "black":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
                x += 50
        blocked = False
        y = ory
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y += 50
        blocked = False
        x = orx
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
                y -= 50
        blocked = False
        x = orx
        y = ory
    if color == "white":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x += 50
        blocked = False
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
        blocked = False
        x = ory
    if color == "black":
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y += 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                y -= 50
        blocked = False
        y = ory
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x += 50
        blocked = False
        x = orx
        for piece in impieces:
            if blocked == False:
                if piece[xcor] == x and piece[ycor] == y:
                    for piece in imwpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            places.append(x)
                            places.append(y)
                    for piece in imbpieces:
                        if piece[xcor] == x and piece[ycor] == y:
                            blocked = True
                else:
                    places.append(x)
                    places.append(y)
                x -= 50
        blocked = False
        x = orx
    return places
def kingStep(x, y, color, rochet):
    places = [x + 50, y, x + 50, y + 50, x + 50, y - 50, x - 50, y, x - 50, y + 50, x - 50, y - 50, x, y, x, y + 50,
              x, y - 50, ]
    if color == "white":
        for piece in imwpieces:
            if (piece[xcor] == x and piece[ycor] == y - 50):
                places.remove(x)
                places.remove(y - 50)
            if (piece[xcor] == x and piece[ycor] == y + 50):
                places.remove(x)
                places.remove(y + 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y - 50):
                places.remove(x + 50)
                places.remove(y - 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y + 50):
                places.remove(x + 50)
                places.remove(y + 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y):
                places.remove(x + 50)
                places.remove(y)
            if (piece[xcor] == x - 50 and piece[ycor] == y - 50):
                places.remove(x - 50)
                places.remove(y - 50)
            if (piece[xcor] == x - 50 and piece[ycor] == y + 50):
                places.remove(x - 50)
                places.remove(y + 50)
            if (piece[xcor] == x - 50 and piece[ycor] == y):
                places.remove(x - 50)
                places.remove(y)
    if color == "black":
        for piece in imbpieces:
            if (piece[xcor] == x and piece[ycor] == y - 50):
                places.remove(x)
                places.remove(y - 50)
            if (piece[xcor] == x and piece[ycor] == y + 50):
                places.remove(x)
                places.remove(y + 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y - 50):
                places.remove(x + 50)
                places.remove(y - 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y + 50):
                places.remove(x + 50)
                places.remove(y + 50)
            if (piece[xcor] == x + 50 and piece[ycor] == y):
                places.remove(x + 50)
                places.remove(y)
            if (piece[xcor] == x - 50 and piece[ycor] == y - 50):
                places.remove(x - 50)
                places.remove(y - 50)
            if (piece[xcor] == x - 50 and piece[ycor] == y + 50):
                places.remove(x - 50)
                places.remove(y + 50)
            if (piece[xcor] == x - 50 and piece[ycor] == y):
                places.remove(x - 50)
                places.remove(y)
    return places
# rochet & checkcheck needed

def calc_steps_white(Xcor, Ycor):
    flipvar = 1
    for piece in imwpieces:
        if piece["xcor"] == Xcor and piece["ycor"] == Ycor:
            crtpiece = piece["typ"]
            detpiece = piece
    if crtpiece == "pawn":
        for place in pawnStep(detpiece["xcor"], detpiece["ycor"], "white", detpiece["moved"]):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)
    if crtpiece == "knight":
        for place in knightStep(detpiece["xcor"], detpiece["ycor"], "white"):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)
    if crtpiece == "bishop":
        for place in bishopStep(detpiece["xcor"], detpiece["ycor"], "white"):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)
    if crtpiece == "rook":
        for place in rookStep(detpiece["xcor"], detpiece["ycor"], "white"):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)
    if crtpiece == "queen":
        for place in queenStep(detpiece["xcor"], detpiece["ycor"], "white"):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)
    if crtpiece == "king":
        for place in kingStep(detpiece["xcor"], detpiece["ycor"], "white", detpiece["rochet"]):
            if flipvar == 1:
                x = place
                flipvar = 2
            else:
                y = place
                flipvar = 1
                squarecheck(x, y, bsquares, wsquares)


# Create functions for selecter movement
def br():
    x = selecter.xcor()
    x +=50
    if -175 <= x <= 175:
        selecter.setx(x)
def bl():
    x = selecter.xcor()
    x -= 50
    if -175 <= x <= 175:
        selecter.setx(x)
def bd():
    y = selecter.ycor()
    y -= 50
    if -175 <= y <= 175:
        selecter.sety(y)
def bu():
    y = selecter.ycor()
    y += 50
    if -175 <= y <= 175:
        selecter.sety(y)



# Import and assign images
while niceimgloop == 0:
    bpawnimg = "bpawn.gif"
    screen.addshape(bpawnimg)
    bknightimg = "bknight.gif"
    screen.addshape(bknightimg)
    bbishopimg = "bbishop.gif"
    screen.addshape(bbishopimg)
    brookimg = "brook.gif"
    screen.addshape(brookimg)
    bqueenimg = "bqueen.gif"
    screen.addshape(bqueenimg)
    bkingimg = "bking.gif"
    screen.addshape(bkingimg)
    wpawnimg = "wpawn.gif"
    screen.addshape(wpawnimg)
    wknightimg = "wknight.gif"
    screen.addshape(wknightimg)
    wbishopimg = "wbishop.gif"
    screen.addshape(wbishopimg)
    wrookimg = "wrook.gif"
    screen.addshape(wrookimg)
    wqueenimg = "wqueen.gif"
    screen.addshape(wqueenimg)
    wkingimg = "wking.gif"
    screen.addshape(wkingimg)
    for piece in bpieces:
        if picnum < 8:
            piece.shape(bpawnimg)
        if 10 > picnum >= 8:
            piece.shape(bknightimg)
        if 12 > picnum >= 10:
            piece.shape(bbishopimg)
        if picnum == 14 or picnum == 13:
            piece.shape(brookimg)
        if picnum == 12:
            piece.shape(bqueenimg)
        if picnum == 15:
            piece.shape(bkingimg)
        picnum += 1
    picnum = 0
    for piece in wpieces:
        if picnum < 8:
            piece.shape(wpawnimg)
        if picnum < 10 and picnum >= 8:
            piece.shape(wknightimg)
        if picnum < 12 and picnum >= 10:
            piece.shape(wbishopimg)
        if picnum == 14 or picnum == 13:
            piece.shape(wrookimg)
        if picnum == 12:
            piece.shape(wqueenimg)
        if picnum == 15:
            piece.shape(wkingimg)
        picnum += 1
    niceimgloop += 1

screen.onkey(bu, "Up")
screen.onkey(bd, "Down")
screen.onkey(bl, "Left")
screen.onkey(br, "Right")
# screen.onkey(select, "Enter")


screen.listen()
screen.exitonclick()















