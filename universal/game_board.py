import fields.fcontainer as fc

def draw_board(player):
    y = 525
    x = 785

    while x >= 5:
        if x == 785 and y == 525:
            fc.contain("start", "Start", None, 200, 0, x, y)

        elif x == 5 and y == 525:
            fc.contain("jail", "Jail", None, 50, 0, x, y)

        else:
            fc.genRegularField(x, y, player)

        x -= 130

    y -= 130
    x = 5

    while y >= 5:
        if x == 5 and y == 5:
            fc.contain("freeparking", "Free parking", None, 0, 0, x, y)

        else:
            fc.genRegularField(x, y, player)

        y -= 130

    y = 5
    x += 130

    while x <= 785:
        if x == 785 and y == 5:
            fc.contain("gotojail", "Go to jail", None, 0, 0, x, y)
            
        else:
            fc.genRegularField(x, y, player)

        x += 130

    x = 785
    y += 130

    while y <= 395:
        if x == 785 and y == 5:
            fc.contain("gotojail", "Go to jail", None, 0, 0, x, y)

        else:
            fc.genRegularField(x, y, player)
            
        y += 130