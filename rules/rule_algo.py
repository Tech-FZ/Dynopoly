import fields.fcontainer as fc
import random
import rules.rule_ui as r_ui
import transactions.offers as offer

# Variables we can change
house_price = 50
hotel_price = 100
free_parking = 0

def stockMarketCrash(divisor):
    for field in fc.f_container:
        if field.type == "investment":
            field.price /= divisor
            field.rent /= divisor
            
    r_ui.latest_event = [f"Stock market crashed! Stock has", f"{str(divisor)}x less worth."]
            
def stockMarketGoesUp(multiplier):
    for field in fc.f_container:
        if field.type == "investment":
            field.price *= multiplier
            field.rent *= multiplier
            
    r_ui.latest_event = [f"Stock market went up! Stock has", f"{str(multiplier)}x more worth."]
            
def incomeTax(players, tax):
    global free_parking
    i = 0
    while i > len(players):
        players[list(players.keys())[i - 1 % len(players)]].balance -= tax
        free_parking += tax
        i += 1
        
    r_ui.latest_event = [f"Income tax of {str(tax)} went into free parking."]
        
    """ player = players[list(players.keys())[(turns -1) % len(players)]]
    for player in players:
        player.balance -= tax """
        # insert tax added to free parking here
        
def propertyDamage(field, housesDamaged, hotelDamaged):
    decision = random.randint(0, 1)
    
    if housesDamaged > 0:
        if hotelDamaged:
            r_ui.latest_event = [f"{str(housesDamaged)} house(s) & the hotel in {field.name} damaged."]
            
        else:
            r_ui.latest_event = [f"{str(housesDamaged)} house(s) in {field.name} damaged."]
            
    elif hotelDamaged:
        r_ui.latest_event = [f"Hotel in {field.name} damaged."]
    
    if decision == 0:
        if field.houseCount > 0:
            field.houseCount -= housesDamaged
        
        field.price /= housesDamaged
        field.rent /= housesDamaged
        
        if hotelDamaged:
            field.price -= 40
            field.rent -= 4
            
        r_ui.latest_event.append("Price 40 less. Rent 4 less.")
    
    elif decision == 1:
        if field.owner != "Bank":
            field.owner.balance -= 25 * housesDamaged # Can be changed
            
            if hotelDamaged:
                field.owner.balance -= 50
                
        r_ui.latest_event.append("Repairs: 25 per house & 50 for")
        r_ui.latest_event.append("hotel")
    
def shopOpens(field):
    field.price *= 1.5
    field.rent *= 1.5
    r_ui.latest_event = [f"A shop has opened in {field.name}.", "Price and rent increase by 50 %."]
    
def shopCloses(field):
    field.price /= 1.5
    field.rent /= 1.5
    r_ui.latest_event = [f"A shop has closed in {field.name}.", "Price and rent decrease by 50 %."]
    
def housingCrisis(multiplier):
    global house_price
    global hotel_price
    house_price *= multiplier
    hotel_price *= multiplier
    r_ui.latest_event = [f"A housing crisis is ongoing.", f"Prices for houses & hotels {str(multiplier)}x", "higher."]
    
def housingAbundance(divisor):
    global house_price
    global hotel_price
    house_price /= divisor
    hotel_price /= divisor
    r_ui.latest_event = [f"A housing abundance is ongoing.", f"Prices for houses & hotels {str(divisor)}x", "lower."]
    
def birthday(bd_player, other_players):
    total_bd_money = 0
    
    for player in other_players:
        player.balance -= 10
        total_bd_money += 10
        
    bd_player.balance += total_bd_money
    
    r_ui.latest_event = [f"{bd_player.name}'s birthday - They get 10 dollars from everyone else"]
    
def jailFreeEvent(player):
    get_free = random.randint(0, 12)
    print(get_free)
    
    if get_free == 3 or get_free == 7 or get_free == 12:
        player.jailStatus['in_jail'] = False
        r_ui.latest_event = [f"{player.name} is no longer in jail."]
        
def jailEvent(screen, player, jail, players, dices, jail_fid):
    player.move_to(screen, jail, players=players, dices=dices)
    player.fid = jail_fid
    player.jailStatus['in_jail'] = True
    r_ui.latest_event = [f"{player.name} went to jail."]
    
def eventSelector(screen, jail, players, dices, jail_fid):
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
    10. Jailbreak Event (A prisoner gets out of jail if lucky enough)
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
        
        propertyDamage(st_container[random.randint(0, len(st_container) - 1)], random.randint(1, 4), random.choice([True, False]))
        
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
        
    #elif eventSel == 9:
        # May or may not be removed
        #jailEvent(screen, random.choice(players), jail, players, dices, jail_fid)
        
    """ elif eventSel == 8:
        bd_player_idx = random.randint(1, len(players))
        bd_player = players[bd_player_idx]
        other_players = players.pop(bd_player_idx)
        birthday(bd_player, other_players) """
        
    print(r_ui.latest_event)
    
    ecp = True
    
    while ecp:
        ecp = r_ui.event_card(screen, True)
