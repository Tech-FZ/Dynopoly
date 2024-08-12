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