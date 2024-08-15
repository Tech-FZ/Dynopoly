import fields.fcontainer as fc
import json
import random
import rules.rule_ui as r_ui

def everyStreet():
    streets = []
    
    for field in fc.f_container:
        if field.type == "street":
            streets.append(field)
            
    return streets

def everyProperty(player):
    streets = everyStreet()
    player_won = True
    
    for street in streets:
        if street.owner.name != player.name:
            player_won = False
            break
        
    return player_won

def startPassWithoutMoneySpent(player):    
    if player.money_spent_round == False and player.round_complete:
        return True
    
    elif player.money_spent_round or player.round_complete == False:
        return False
    
def hotel(player):
    streets = everyStreet()
    player_won = False
    
    for street in streets:
        if street.owner.name == player.name and street.hotelAvailable == True:
            player_won = True
            break
        
    return player_won

def genWinningConditions(player):
    f = open('player/winConditions.json')
    win_conditions = json.load(f)
    possible_conditions = ["1", "3", "6"] # temporary tuple to make sure the game is doable
    
    for k in range(2):
        i = random.randint(0, len(possible_conditions) - 1)
        player.win_condition.append(win_conditions[possible_conditions[i]])
        possible_conditions.pop(i)
    
def checkWinningConditions(screen, player):
    f = open('player/winConditions.json')
    win_conditions = json.load(f)
    
    for win_cond in player.win_condition:
        if win_cond == win_conditions["1"]:
            con = everyProperty(player)
            
        elif win_cond == win_conditions["3"]:
            con = startPassWithoutMoneySpent(player)
            player.round_complete = False
            
        elif win_cond == win_conditions["6"]:
            con = hotel(player)
            
        if con:
            player.win_condition.remove(win_cond)
            
        if len(player.win_condition) <= 0:
            r_ui.latest_event = [f"{player.name} won!"]
            phase = True
            
            while phase:
                phase = r_ui.event_card(screen, phase)