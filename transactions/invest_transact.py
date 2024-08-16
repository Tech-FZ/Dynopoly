def invest(player, investment):
    if player.balance >= investment.price:
        player.balance -= round(investment.price,2)
        player.money_spent_round = True
        if investment.owner.name != "Bank":
            player.successful_trade = True
            
        investment.change_owner(player)
        player.properties.append(investment)
        
def earn_money(player, investment):
    player.balance -= round((1+investment.rent/100) * investment.price,2)
    player.money_spent_round = True
    investment.owner.balance += round((1+investment.rent/100) * investment.price,2)