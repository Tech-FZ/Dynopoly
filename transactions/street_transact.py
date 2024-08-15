import fields.fcontainer as fc
import rules.rule_algo as r_algo
import transactions.offers as offer

def buyStreet(player, street):
    if player.balance >= street.price and street.owner is not None:
        player.balance -= street.price
        if street.owner.name != "Bank":
            player.successful_trade = True
            
        street.change_owner(player)
        player.properties.append(street)
        player.money_spent_round = True

def payRent(player, street):
    if street.owner is not None:
        print(street.rent)
        print(street.houseCount)
        player.balance -= street.rent
        street.owner.balance += street.rent
        player.money_spent_round = True
    else:
        pass

def buyHouse(player, street):
    if player.name == street.owner and player.balance >= r_algo.house_price:
        player.balance -= r_algo.house_price
        street.houseCount += 1
        street.price += r_algo.house_price * 1.2
        street.rent += r_algo.house_price / 8
        player.money_spent_round = True

def buyHotel(player, street):
    if player.name == street.owner and player.balance >= r_algo.hotel_price and street.hotelAvailable == False:
        player.balance -= r_algo.hotel_price
        street.hotelAvailable = True
        street.price += r_algo.hotel_price * 1.2
        street.rent += r_algo.hotel_price / 8
        player.money_spent_round = True