def invest(player, investment):
    if player.balance >= investment.price:
        player.balance -= investment.price
        investment.change_owner(player)
        # investment.owner == player
        player.properties.append(investment)
        
def earn_money(player, investment):
    player.balance -= ((1+investment.rent) * investment.price)
    investment.owner.balance += ((1+investment.rent) * investment.price)