import fields.fcontainer as fc
import random

# Variables we can change
house_price = 50
hotel_price = 100

def stockMarketCrash(divisor):
    for field in fc.f_container:
        if field.type == "investment":
            field.price /= divisor
            field.rent /= divisor
            
def stockMarketGoesUp(multiplier):
    for field in fc.f_container:
        if field.type == "investment":
            field.price *= multiplier
            field.rent *= multiplier
            
def incomeTax(players, tax):
    for player in players:
        player.balance -= tax
        # insert tax added to free parking here
        
def propertyDamage(field, housesDamaged, hotelDamaged):
    decision = random.randint(0, 1)
    
    if decision == 0:
        if field.houseCount > 0:
            field.houseCount -= housesDamaged
        
        field.price /= housesDamaged
        field.rent /= housesDamaged
        
        if hotelDamaged:
            field.price -= 40
            field.rent -= 4
    
    elif decision == 1:
        if field.owner != "Bank":
            field.owner.balance -= 25 * housesDamaged # Can be changed
            
            if hotelDamaged:
                field.owner.balance -= 50
    
def shopOpens(field):
    field.price *= 1.5
    field.rent *= 1.5
    
def shopCloses(field):
    field.price /= 1.5
    field.rent /= 1.5
    
def housingCrisis(multiplier, house_pr=house_price, hotel_pr=hotel_price):
    house_pr *= multiplier
    hotel_pr *= multiplier
    
def housingAbundance(divisor, house_pr=house_price, hotel_pr=hotel_price):
    house_pr /= divisor
    hotel_pr /= divisor
    
def birthday(bd_player, other_players):
    total_bd_money = 0
    
    for player in other_players:
        player.balance -= 10
        total_bd_money += 10
        
    bd_player.balance += total_bd_money
    
def jailFreeEvent(player):
    get_free = random.randint(0, 12)
    print(get_free)
    
    if get_free == 3 or get_free == 7 or get_free == 12:
        player.isInJail = False
        
def jailEvent(screen, player, jail, players, dices, jail_fid):
    player.move_to(screen, jail, players=players, dices=dices)
    player.fid = jail_fid
    player.isInJail = True
    
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
        stockMarketCrash(random.randint(1, 4) + random.random())
        
    elif eventSel == 1:
        stockMarketGoesUp(random.randint(1, 4) + random.random())
        
    elif eventSel == 2:
        incomeTax(players, random.randint(50, 200))
        
    elif eventSel == 3:
        # Temporary, needs to be replaced
        propertyDamage(fc.f_container[random.randint(0, len(fc.f_container) - 1)], random.randint(1, 4), random.choice([True, False]))
        
    elif eventSel == 4:
        shopOpens(fc.f_container[random.randint(0, len(fc.f_container) - 1)])
        
    elif eventSel == 5:
        shopCloses(fc.f_container[random.randint(0, len(fc.f_container) - 1)])
        
    elif eventSel == 6:
        housingCrisis(random.randint(1, 4) + random.random())
        
    elif eventSel == 7:
        housingAbundance(random.randint(1, 4) + random.random())
        
    elif eventSel == 8:
        bd_player_idx = random.randint(0, len(players) - 1)
        bd_player = players[bd_player_idx]
        other_players = players.pop(bd_player_idx)
        birthday(bd_player, other_players)
        
    elif eventSel == 9:
        # May or may not be removed
        jailEvent(screen, random.choice(players), jail, players, dices, jail_fid)