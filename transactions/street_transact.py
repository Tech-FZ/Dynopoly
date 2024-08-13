import fields.fcontainer as fc

def buyStreet(player, street):
    if player.balance >= street.price and street.owner is not None:
        player.balance -= street.price
        street.change_owner(player)
        player.properties.append(street)

def payRent(player, street):
    if street.owner is not None:
        print(street.rent)
        print(street.houseCount)
        player.balance -= street.rent
        street.owner.balance += street.rent
    else:
        pass

def buyHouse(player, street):
    if player.name == street.owner and player.balance >= 50: # house price, can be changed
        player.balance -= 50
        street.houseCount += 1
        # street.rent should increase

def buyHotel(player, street):
    if player.name == street.owner and player.balance >= 75 and street.hotelAvailable == False and street.houseCount == 4: # hotel price, can be changed
        player.balance -= 75
        street.hotelAvailable = True
        street.houseCount = 0
        # street.rent should increase