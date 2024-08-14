# Third-party libraries
import pygame
import json
import random

# Other code files
import universal.side_bar as sb
import fields.fields as fields
import fields.fcontainer as fc
import player.player as pl
import player.player_card as pc
import dice.dice as dc
import universal.button as btn
import universal.game_board as gb
import transactions.street_transact as st_transact
import transactions.invest_transact as invest_transact
import transactions.offers as offer
import items.property as prop
import items.investment as invest
import rules.rule_ui as r_ui
import rules.rule_algo as r_algo

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dynopoly")
clock = pygame.time.Clock()
running = True

#Defined the bank as a player type so as to assign initial ownership
bank = pl.Player("Bank", "white")
bank.balance = 1000000


player1 = pl.Player("Nicolas", "red")
f = open('player/winConditions.json')
win_conditions = json.load(f)
player1.win_condition.append(win_conditions["1"])
player1.win_condition.append(win_conditions["2"])

player2 = pl.Player("Player 2", "blue")
player2.win_condition.append(win_conditions["1"])
player2.win_condition.append(win_conditions["2"])
player2.position = pygame.Vector2(860, 600)

dices = []
players ={}

dc1 = dc.Dice()

dc2 = dc.Dice()
dc2.x = 175

dices.append(dc1)
dices.append(dc2)

players[1] = player1
players[2] = player2

# Initialize game fields
gb.draw_board(bank)

# Function to spawn game components
def display_board(screen,turns,dices):
    screen.fill("purple")
    
    # fc.genBoard(screen)
    
    fc.genBoard(screen),
    sb.sb_setup(screen),
    r_ui.ruleCard(screen),
    pc.player_card(screen, players[(turns-1) % len(players)+1])
    pc.win_condition_Card(screen,  players[(turns-1) % len(players)+1])

    # Dice spawning
    for dice in dices:
        dice.spawnDice(screen)
        
    rodi_btn.updateButton(rodi_btn.bg_colour, rodi_btn.txt_colour)
        

#Initialize jail for moving mechanism
for index, field in enumerate(fc.f_container):
    # jail = fields.Field(5,525,None)
    if field.type == "jail":
        jail = field
        jail_fid = index

turns = 1

def afterTurn(player):
    trade_phase = True
    
    while trade_phase:
        if fc.f_container[player.fid].owner is None:
            break
            
        elif fc.f_container[player.fid].type == "street":
            if fc.f_container[player.fid].owner.name == "Bank":
                trade_phase = offer.offer_card(screen, 
                                               phase = trade_phase,
                                               ftc = st_transact.buyStreet, 
                                               kw_args={"player":player,
                                               "street":fc.f_container[player.fid]} )
                # st_transact.buyStreet(player, fc.f_container[player.fid])
            elif fc.f_container[player.fid].owner == player:
                break # Insert code to buy stuff here
            
            else:
                st_transact.payRent(player, fc.f_container[player.fid])
                print(f"{player.name} Paid rent to {fc.f_container[player.fid].owner.name}")
                
        elif fc.f_container[player.fid].type == "investment":
            if fc.f_container[player.fid].owner.name == "Bank":
                trade_phase = offer.offer_card(screen, 
                                               phase = trade_phase,
                                               ftc = invest_transact.invest, 
                                               kw_args={"player":player,
                                               "investment":fc.f_container[player.fid]} )
                # invest_transact.invest(player, fc.f_container[player.fid])
                
            elif fc.f_container[player.fid].owner != player and not None:
                invest_transact.earn_money(player, fc.f_container[player.fid])
                print(f"{player.name} Paid interest to {fc.f_container[player.fid].owner.name}")
                
        else: 
            break

def rollDices(players=players):
    global turns
    player = players[list(players.keys())[(turns -1) % len(players)]]
    player_drunk = False
    
    if player.drunkStatus > 0:
        player_drunk = True
        player.drunkStatus -= 1

    total_value = 0
    
    if player.jailStatus['in_jail']:
        r_algo.jailFreeEvent(player)
    
    if player.jailStatus['in_jail'] == False:
        for dice in dices:
            dice.rollDice(screen)
            total_value += dice.value

        new_fid = player.fid + total_value
    
        if new_fid >= len(fc.f_container):
            new_fid = 0 + (new_fid - len(fc.f_container))
            player.balance += 200
    
        while player.fid != new_fid:
            if player.fid == len(fc.f_container)-1:
                player.fid = 0
                player.move_to(screen,
                               turns, 
                               display_board, 
                               fc.f_container[player.fid], 
                               players=players, 
                               dices=dices)
        
            else:
                player.fid += 1
                player.move_to(screen,
                               turns, 
                               display_board, 
                               fc.f_container[player.fid], 
                               players=players, 
                               dices=dices)
            
        afterTurn(player)
        if fc.f_container[player.fid].type == "bar":
            player.balance -= r_algo.bar_price
            player.drunkStatus = 3
            
        elif fc.f_container[player.fid].type == "freeparking":
            player.balance += r_algo.free_parking
            r_algo.free_parking = 0
            
        player_buys_anyway = random.randint(0, 1)
            
        if player_drunk and fc.f_container[player.fid].owner.name == "Bank" and player_buys_anyway == 1:
            if fc.f_container[player.fid].type == "street":
                st_transact.buyStreet(player, fc.f_container[player.fid])
                
            elif fc.f_container[player.fid].type == "investment":
                invest_transact.invest(player, fc.f_container[player.fid])
        
        print(player.jailStatus)
        r_algo.eventSelector(screen, jail, players, dices, jail_fid)
        turns += 1
        
# insert buttons here
rodi_btn = btn.Button(
    screen,
    "Roll dice",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    205,
    480,
    65,
    25,
    rollDices
)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        rodi_btn.checkClick(event)

    display_board(screen, turns, dices)
    # # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # # RENDER YOUR GAME HERE
    # sb.sb_setup(screen)
    # # for fld in fc.f_container:
    # #     fld.field_placement(screen)
    # fc.genBoard(screen)
    # r_ui.ruleCard(screen)
    
    #player components
    player1.spawn(screen)
    player2.spawn(screen)
    # pc.player_card(screen, players[(turns-1) % len(players)+1])
    # pc.win_condition_Card(screen,  players[(turns-1) % len(players)+1])

    
    # dc1.spawnDice(screen)
    # dc2.spawnDice(screen)

    # rodi_btn.updateButton(rodi_btn.bg_colour, rodi_btn.txt_colour)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
