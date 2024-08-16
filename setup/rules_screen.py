import json
import pygame

def show_rules(screen):
    running = True

    # Load rules from JSON file
    with open("setup/rules.json", "r") as file:
        rules_data = json.load(file)

    # Split rules into two parts
    first_half = {
        "classic_rules": rules_data["classic_rules"],
        "jail_twist": []
    }
    
    second_half = {
        "classic_rules": [],
        "jail_twist": rules_data["jail_twist"],
        "dynamic_rules": rules_data["dynamic_rules"]
    }

    # Define fonts
    title_font = pygame.font.SysFont("Arial", 40)
    subtitle_font = pygame.font.SysFont("Arial", 30)
    rules_font = pygame.font.SysFont("Arial", 20)
    bold_font = pygame.font.SysFont("Arial", 20, True)

    # Initialize the screen part
    screen_part = 1

    # Main loop for displaying the rules screen
    while running:
        screen.fill("purple")
        
        # Draw the rules box
        rules_width = screen.get_width() - 10
        rules_height = screen.get_height() - 10
        rules_location = pygame.Vector2(5, 5)
        pygame.draw.rect(screen, "gray", pygame.Rect(rules_location.x, rules_location.y, rules_width, rules_height))

        # Render the title, subtitle, and "Rules" header
        screen.blit(title_font.render(rules_data["title"], True, (0, 0, 0)), pygame.Vector2(50, 20))
        screen.blit(subtitle_font.render(rules_data["subtitle"], True, (0, 0, 0)), pygame.Vector2(50, 70))
        screen.blit(bold_font.render("Rules", True, (0, 0, 0)), pygame.Vector2(50, 120))
        
        # Render rules based on the screen part
        if screen_part == 1:
            render_rules(screen, first_half, bold_font, rules_font, y_offset=170)
            screen.blit(title_font.render("But there's a twist...", True, (0,0,0)), pygame.Vector2(screen.get_width()/2-100))
            next_surface = rules_font.render("Press N for Next", True, (0, 0, 0))
            screen.blit(next_surface, pygame.Vector2(rules_width - 200, rules_height - 50))
        else:
            render_rules(screen, second_half, bold_font, rules_font, y_offset=170)
            main_menu = rules_font.render("Press ESC for Main Menu", True, (0, 0, 0))
            screen.blit(main_menu, pygame.Vector2(50, rules_height - 50))
            
            back_surface = rules_font.render("Press B to go Back", True, (0, 0, 0))
            screen.blit(back_surface, pygame.Vector2(rules_width - 200, rules_height - 50))

        pygame.display.flip()

        # Event handling for navigating between the two screens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if screen_part == 1 and event.key == pygame.K_n:  # Go to the second screen
                    screen_part = 2
                elif screen_part == 2 and event.key == pygame.K_b:  # Go back to the first screen
                    screen_part = 1
                elif event.key == pygame.K_ESCAPE:  # Exit the rules screen
                    running = False

def render_rules(screen, rules_data, bold_font, rules_font, y_offset):
    # Render Classic Rules
    if rules_data["classic_rules"]:
        screen.blit(bold_font.render("Classic Rules:", True, (0, 0, 0)), pygame.Vector2(50, y_offset))
        y_offset += 30
        for rule in rules_data["classic_rules"]:
            if isinstance(rule, str):
                screen.blit(rules_font.render(rule, True, (0, 0, 0)), pygame.Vector2(70, y_offset))
                y_offset += 30
            elif isinstance(rule, dict):
                for key, subrules in rule.items():
                    screen.blit(rules_font.render(key + ":", True, (0, 0, 0)), pygame.Vector2(90, y_offset))
                    y_offset += 30
                    for subrule in subrules:
                        screen.blit(rules_font.render("- " + subrule, True, (0, 0, 0)), pygame.Vector2(110, y_offset))
                        y_offset += 30

    # Render Jail Twist
    if rules_data["jail_twist"]:
        y_offset += 10
        screen.blit(bold_font.render("Jail Twist:", True, (0, 0, 0)), pygame.Vector2(50, y_offset))
        y_offset += 30
        for rule in rules_data["jail_twist"]:
            if isinstance(rule, str):
                screen.blit(rules_font.render(rule, True, (0, 0, 0)), pygame.Vector2(70, y_offset))
                y_offset += 30
            elif isinstance(rule, dict):
                for key, subrules in rule.items():
                    screen.blit(rules_font.render(key + ":", True, (0, 0, 0)), pygame.Vector2(90, y_offset))
                    y_offset += 30
                    for subrule in subrules:
                        screen.blit(rules_font.render("- " + subrule, True, (0, 0, 0)), pygame.Vector2(110, y_offset))
                        y_offset += 30

    # Render Dynamic Rules
    if rules_data.get("dynamic_rules"):
        y_offset += 10
        screen.blit(bold_font.render("Dynamic Rules:", True, (0, 0, 0)), pygame.Vector2(50, y_offset))
        y_offset += 30
        for rule in rules_data["dynamic_rules"]:
            if isinstance(rule, str):
                screen.blit(rules_font.render(rule, True, (0, 0, 0)), pygame.Vector2(70, y_offset))
                y_offset += 30
            elif isinstance(rule, dict):
                for key, subrules in rule.items():
                    screen.blit(rules_font.render(key + ":", True, (0, 0, 0)), pygame.Vector2(90, y_offset))
                    y_offset += 30
                    for subrule in subrules:
                        screen.blit(rules_font.render("- " + subrule, True, (0, 0, 0)), pygame.Vector2(110, y_offset))
                        y_offset += 30
