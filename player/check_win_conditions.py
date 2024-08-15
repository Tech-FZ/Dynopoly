import fields.fcontainer as fc
import json
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
    if player.money_spent_round == False:
        return True
    
    elif player.money_spent_round:
        return False
    
def hotel(player):
    streets = everyStreet()
    player_won = False
    
    for street in streets:
        if street.owner.name == player.name and street.hotelAvailable == True:
            player_won = True
            break
        
    return player_won
    
def checkWinningConditions(screen, player):
    f = open('player/winConditions.json')
    win_conditions = json.load(f)
    
    for win_cond in player.win_condition:
        if win_cond == win_conditions["1"]:
            con = everyProperty(player)
            
        elif win_cond == win_conditions["3"]:
            con = startPassWithoutMoneySpent(player)
            
        elif win_cond == win_conditions["6"]:
            con = hotel(player)
            
        if con:
            player.win_conditions.remove(win_cond)
            
        if len(player.win_condition) <= 0:
            r_ui.latest_event = [f"{player.name} won!"]
            phase = True
            
            while phase:
                phase = r_ui.event_card(screen, phase)