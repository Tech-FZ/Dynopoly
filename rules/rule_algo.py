import fields.fcontainer as fc
import random
import rules.rule_ui as r_ui

# Variables we can change
house_price = 50
hotel_price = 100
free_parking = 0
fine = 100
bar_price = 5

def stockMarketCrash(divisor):
    for field in fc.f_container:
        if field.type == "investment":
            field.price = round(field.price / divisor , 2)
            field.rent = round(field.rent / divisor , 2)
            
    r_ui.latest_event = [f"Stock market crashed! Stock has", f"{str(divisor)}x less worth."]
            
def stockMarketGoesUp(multiplier):
    for field in fc.f_container:
        if field.type == "investment":
            field.price = round(field.price / multiplier , 2)
            field.rent = round(field.rent / multiplier , 2)
            
    r_ui.latest_event = [f"Stock market went up! Stock has", f"{str(multiplier)}x more worth."]
            
def incomeTax(players, tax):
    global free_parking
    i = 0
    while i < len(players):
        players[list(players.keys())[i - 1 % len(players)]].balance -= tax
        free_parking += tax
        players[list(players.keys())[i - 1 % len(players)]].money_spent_round = True
        i += 1
        
    r_ui.latest_event = [f"Income tax of {str(tax)} per player", "went into free parking."]
        
def propertyDamage(field, housesDamaged, hotelDamaged):
    decision = random.choice([0,0.5,1])
    
    if housesDamaged > 0:
        if hotelDamaged and field.hotelAvailable:
            r_ui.latest_event = [f"{str(housesDamaged)} house(s) & the hotel in {field.name} damaged."]
            
        else:
            r_ui.latest_event = [f"{str(housesDamaged)} house(s) in {field.name} damaged."]
            
    elif hotelDamaged and field.hotelAvailable:
        r_ui.latest_event = [f"Hotel in {field.name} damaged."]
    
    if decision == 0:
        if field.houseCount > 0:
            field.houseCount -= housesDamaged
        
            field.price = round(field.price / housesDamaged , 2)
            field.rent = round(field.rent / housesDamaged , 2)
        
        if hotelDamaged and field.hotelAvailable:
            field.hotelAvailable = False
            field.price -= 40
            field.rent -= 4
            
        r_ui.latest_event.append("Price and rent decrease.")
    
    elif decision == 1:
        if field.owner != "Bank":
            field.owner.balance -= house_price * housesDamaged
            
            if hotelDamaged and field.hotelAvailable:
                field.owner.balance -= hotel_price
                
            field.owner.money_spent_round = True
                
        r_ui.latest_event.append("Repairs to be done")
    
def shopOpens(field):
    field.price = round(field.price * 1.5 , 2)
    field.rent = round(field.rent * 1.5 , 2)
    r_ui.latest_event = [f"A shop has opened in {field.name}.", "Price and rent increase by 50 %."]
    
def shopCloses(field):
    field.price = round(field.price / 1.5 , 2)
    field.rent = round(field.rent / 1.5 , 2)
    r_ui.latest_event = [f"A shop has closed in {field.name}.", "Price and rent decrease by 50 %."]
    
def housingCrisis(multiplier):
    global house_price
    global hotel_price
    house_price = round(house_price*multiplier)
    hotel_price = round(hotel_price*multiplier)
    r_ui.latest_event = [f"A housing crisis is ongoing.", f"Prices for houses & hotels {str(multiplier)}x", "higher."]
    
def housingAbundance(divisor):
    global house_price
    global hotel_price
    house_price = round(house_price*divisor)
    hotel_price = round(hotel_price*divisor)
    r_ui.latest_event = [f"A housing abundance is ongoing.", f"Prices for houses & hotels {str(divisor)}x", "lower."]
    
def birthday(bd_player, other_players):
    total_bd_money = 0
    i = 1
    
    while i <= len(other_players):
        if other_players[i].name != bd_player.name:
            other_players[i].balance -= 10
            
        i += 1
        
    bd_player.balance += total_bd_money
    
    r_ui.latest_event = [f"{bd_player.name}'s birthday - They get 10", "dollars from everyone else"]
    
def jailFreeEvent(screen, turns, board, player, players, dices, doubles, total_value):
    if doubles:
        player.jailStatus = False
        player.jailTurns = 1
        new_fid = player.fid + total_value
        
    
        if new_fid >= len(fc.f_container):
            new_fid = 0 + (new_fid - len(fc.f_container))
            player.balance += 200
    
        while player.fid != new_fid:
            if player.fid == len(fc.f_container)-1:
                player.fid = 0
                player.move_to(screen,
                               turns, 
                               board, 
                               fc.f_container[player.fid], 
                               players=players, 
                               dices=dices)
        
            else:
                player.fid += 1
                player.move_to(screen,
                               turns, 
                               board, 
                               fc.f_container[player.fid], 
                               players=players, 
                               dices=dices)
    elif player.jailTurns == 3:
        player.jailTurns = 1
        player.balance -= fine
        player.money_spent_round = True
        player.jailStatus = False
        r_ui.latest_event  = [f"{player.name} paid a fine, he is free"]
        
    else:
        player.jailTurns += 1
        get_free = random.randint(0, 12)
        if get_free == 3 or get_free == 7 or get_free == 12:
            player.jailStatus = False
            r_ui.latest_event = [f"{player.name} is no longer in jail."]
        
def jailEvent(screen, player, jail, players, dices, jail_fid, turns, board):
    player.move_to(screen, turns, board, jail, players=players, dices=dices)
    player.fid = jail_fid
    player.jailStatus = True
    player.jailTurns = 1
    r_ui.latest_event = [f"{player.name} went to jail."]
    
def checkBankruptcy(screen, player, bank, players, turns):
    if player.balance < 0:
        for field in fc.f_container:
            if field.owner == player:
                field.owner = bank
                
        players.pop((turns -1) % len(players)+1)
        
    if len(players) == 1:
        pk = players.keys()
        r_ui.latest_event = [f"{players[pk[0]]} won"]        
        ecp = True
    
        while ecp:
            ecp = r_ui.event_card(screen, True, exit)
    
def eventSelector(screen, jail, players, dices, jail_fid, turns, board, player):
    """
    Event IDs
    0. Stock Market Crash
    1. Stock Market Goes Up
    2. Income Tax
    3. Property Damage
    4. Shop opens
    5. Shop Closure
    6. Housing Crisis
    7. Housing Abundance
    8. Birthday
    9. Jail Event (A player is brought to jail)
    """
    
    eventSel = random.randint(0, 9)
    
    if eventSel == 0:
        stockMarketCrash(round(random.randint(1, 4) + random.random(), 2))
        
    elif eventSel == 1:
        stockMarketGoesUp(round(random.randint(1, 4) + random.random(), 2))
        
    elif eventSel == 2:
        incomeTax(players, random.randint(50, 200))
        
    elif eventSel == 3:
        st_container = []
        
        for field in fc.f_container:
            if field.type == "street":
                st_container.append(field)
        
        street_chosen = st_container[random.randint(0, len(st_container) - 1)]
        
        if street_chosen.houseCount > 0 or street_chosen.hotelAvailable:
            try:
                propertyDamage(street_chosen, random.randint(1, street_chosen.houseCount), random.choice([True, False]))
                
            except:
                propertyDamage(street_chosen, 1, random.choice([True, False]))
        
    elif eventSel == 4:
        st_container = []
        
        for field in fc.f_container:
            if field.type == "street":
                st_container.append(field)
                
        shopOpens(st_container[random.randint(0, len(st_container) - 1)])
        
    elif eventSel == 5:
        st_container = []
        
        for field in fc.f_container:
            if field.type == "street":
                st_container.append(field)
                
        shopCloses(st_container[random.randint(0, len(st_container) - 1)])
        
    elif eventSel == 6:
        housingCrisis(round(random.randint(1, 4) + random.random(), 2))
        
    elif eventSel == 7:
        housingAbundance(round(random.randint(1, 4) + random.random(), 2))
        
    elif eventSel == 9:
        jailEvent(screen, player, jail, players, dices, jail_fid, turns, board)
        
    elif eventSel == 8:
        bd_player_idx = random.randint(1, len(players))
        bd_player = players[bd_player_idx]
        birthday(bd_player, players)
    
    ecp = True
    
    while ecp:
        ecp = r_ui.event_card(screen, True)
