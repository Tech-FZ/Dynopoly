import fields.fcontainer as fc

def buyStreet(player, street):
    if player.balance >= street.price:
        player.balance -= street.price
        street.owner == player

def payRent(player, street):
    player.balance -= street.rent
    street.owner.balance += street.rent

def buyHouse(player, street):
    if player.name == street.owner and player.balance >= 50: # house price, can be changed
        player.balance -= 50
        street.houseCount += 1
        # street.rent should increase

def buyHotel(player, street):
    if player.name == street.owner and player.balance >= 75 and street.hotelAvailable == False: # hotel price, can be changed
        player.balance -= 75
        street.hotelAvailable = True
        # street.rent should increase