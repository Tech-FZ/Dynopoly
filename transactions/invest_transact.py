def invest(player, investment):
    if player.balance >= investment.price:
        player.balance -= investment.price
        player.money_spent_round = True
        investment.change_owner(player)
        player.properties.append(investment)
        
def earn_money(player, investment):
    player.balance -= ((1+investment.rent/100) * investment.price)
    player.money_spent_round = True
    investment.owner.balance += ((1+investment.rent/100) * investment.price)