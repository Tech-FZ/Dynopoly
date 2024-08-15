from typing import List
import pygame
import universal.fonts as fonts

def welcome_screen(screen):
    running = True
    # Loop for handling the welcome screen
    while running:
        # Fill the screen with a background color
        screen.fill("purple")
        
        # Define the dimensions and position of the welcome box
        welcome_width = screen.get_width() - 10
        welcome_height = screen.get_height() - 10
        welcome_location = pygame.Vector2(5, 5)
        
        # Draw the welcome box
        pygame.draw.rect(screen, "gray", pygame.Rect(welcome_location.x, welcome_location.y, welcome_width, welcome_height))
        
        # Render the welcome header text
        welcome_header = fonts.small_font.render("Welcome to", False, (0, 0, 0))
        wheader_location = pygame.Vector2((welcome_width / 2) - 50, 20)
        screen.blit(welcome_header, wheader_location)
        
        # Render the game title
        welcome_header2 = fonts.default_font.render("DYNOPOLY", False, (0, 0, 0))
        w2header_location = pygame.Vector2((welcome_width / 2) - 50, 50)
        screen.blit(welcome_header2, w2header_location)
        
        # Render the menu options
        menu_options = ["1. New Game", "2. Rules", "3. Exit"]
        for i, option in enumerate(menu_options):
            option_surface = fonts.small_font.render(option, False, (0, 0, 0))
            option_location = pygame.Vector2((welcome_width / 2) - 50, 100 + i * 30)
            screen.blit(option_surface, option_location)

        pygame.display.flip()
        
        # Event handling for selecting menu options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # New Game
                    return setup_game(screen)
                elif event.key == pygame.K_2:  # Rules
                    show_rules(screen)
                elif event.key == pygame.K_3:  # Exit
                    pygame.quit()
                    exit()
                else:
                    running = False
                    
                    
    return []
                

def setup_game(screen):
    # Code to setup the game (player selection, etc.)
    pass

def show_rules(screen):
    # Code to display the rules
    pass
