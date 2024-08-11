import pygame
import universal.fonts as fonts
from .player import Player

def player_card(screen, player: Player):
    # Card dimensions and location
    card_width = int(screen.get_width() / 4)
    card_x = (screen.get_width() / 4) * 3  # x position for the card
    card_y = 60  # y position for the card
    card_height = 120

    # Draw the card background
    pygame.draw.rect(screen, "white", pygame.Rect(card_x, card_y, card_width, card_height))

    # Render the text for the player's details
    player_name = fonts.default_font.render(f"Player: {player.name}", False, "black")
    player_property_count = fonts.default_font.render(f"No. of Properties: {len(player.properties)}", False, "black")
    player_balance = fonts.default_font.render(f"Balance: {player.balance}", False, "black")

    # Define positions for the text
    name_position = pygame.Vector2(card_x + 10, card_y + 10)  # 10 pixels padding
    property_position = pygame.Vector2(card_x + 10, card_y + 40)
    balance_position = pygame.Vector2(card_x + 10, card_y + 70)

    # Blit each text surface onto the screen at the calculated positions
    screen.blit(player_name, name_position)
    screen.blit(player_property_count, property_position)
    screen.blit(player_balance, balance_position)

def win_condition_Card(screen, player:Player):
    card_width = int(screen.get_width() / 4)
    card_x = (screen.get_width() / 4) * 3  # x position for the card
    card_y = 240  # y position for the card
    card_height = 150
    
    pygame.draw.rect(screen, "white", pygame.Rect(card_x, card_y, card_width, card_height))
    win_card_header = fonts.default_font.render("Win Conditions", False, "black")
    header_location = pygame.Vector2(card_x+90, card_y-45)
    screen.blit(win_card_header, header_location)
    
    for index, condition in enumerate(player.win_condition):
        win_card_position = pygame.Vector2(card_x + 10, card_y + 10) 
        win_condition = fonts.default_font.render(f"{index+1}: {condition}", False, "black")
        screen.blit(win_condition, win_card_position)
        
        card_y += 30