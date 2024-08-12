import fields.fcontainer as fc
import rules.rule_algo as r_algo

def buyStreet(player, street):
    if player.balance >= street.price:
        player.balance -= street.price
        street.owner == player

def payRent(player, street):
    player.balance -= street.rent
    street.owner.balance += street.rent

def buyHouse(player, street):
    if player.name == street.owner and player.balance >= r_algo.house_price:
        player.balance -= r_algo.house_price
        street.houseCount += 1
        street.price += r_algo.house_price * 1.2
        street.rent += r_algo.house_price / 8

def buyHotel(player, street):
    if player.name == street.owner and player.balance >= r_algo.hotel_price and street.hotelAvailable == False:
        player.balance -= r_algo.hotel_price
        street.hotelAvailable = True
        street.price += r_algo.hotel_price * 1.2
        street.rent += r_algo.hotel_price / 8