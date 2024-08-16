import fields.fcontainer as fc
import rules.rule_algo as r_algo
import transactions.offers as offer

def buyStreet(player, street):
    if player.balance >= street.price and street.owner is not None:
        player.balance -= round(street.price,2)
        if street.owner.name != "Bank":
            player.successful_trade = True
            
        street.change_owner(player)
        player.properties.append(street)
        player.money_spent_round = True

def payRent(player, street):
    if street.owner is not None:
        player.balance -= round(street.rent,2)
        street.owner.balance += street.rent
        player.money_spent_round = True
    else:
        pass

def buyHouse(player, street):
    if player.name == street.owner and player.balance >= r_algo.house_price:
        player.balance -= r_algo.house_price
        street.houseCount += 1
        street.price += round((r_algo.house_price * 1.2),2)
        street.rent += round((r_algo.house_price / 8),2)
        player.money_spent_round = True

def buyHotel(player, street):
    if player.name == street.owner and player.balance >= r_algo.hotel_price and street.hotelAvailable == False:
        player.balance -= r_algo.hotel_price
        street.hotelAvailable = True
        street.price += round((r_algo.hotel_price * 1.2),2)
        street.rent += round((r_algo.hotel_price / 8),2)
        player.money_spent_round = True