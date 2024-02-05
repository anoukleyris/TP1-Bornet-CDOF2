import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 400, 400
block_size = 20
speed = 8
running = False  # Pour contrôler si le jeu est en cours ou non (issue 3)

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Fonction pour démarrer ou arrêter le jeu (issue 3)
def toggle_game_state():
    global running
    running = not running

# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()

# Initialisation de l'écran
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initialisation du serpent
snake = [(width // 2, height // 2)]
snake_direction = (block_size, 0)

# Initialisation de la pomme
apple = (random.randint(0, (width - block_size) // block_size) * block_size,
         random.randint(0, (height - block_size) // block_size) * block_size)

# Variable pour suivre l'état du texte "Press Enter to begin"
show_start_text = True

# Création d'un bouton "Quit" rectangulaire
quit_button_rect = pygame.Rect(width - 100, 10, 90, 40)
quit_button_color = white

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_game_state() #issue 3
                show_start_text = False  # Cacher le texte quand le jeu est démarré
            elif event.key == pygame.K_RETURN and not running:
                toggle_game_state() # Démarrer le jeu en appuyant sur Entrée
                show_start_text = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button_rect.collidepoint(event.pos):
                quit_game()

    if running: #issue 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_direction != (block_size, 0):
            snake_direction = (-block_size, 0)
        elif keys[pygame.K_RIGHT] and snake_direction != (-block_size, 0):
            snake_direction = (block_size, 0)
        elif keys[pygame.K_UP] and snake_direction != (0, block_size):
            snake_direction = (0, -block_size)
        elif keys[pygame.K_DOWN] and snake_direction != (0, -block_size):
            snake_direction = (0, block_size)

        # Mise à jour de la position du serpent
        x, y = snake[0]
        new_head = (x + snake_direction[0], y + snake_direction[1])

        # Vérification des collisions avec les bords
        if (
            new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height
        ):
            quit_game()

        snake.insert(0, new_head)

        # Vérification des collisions avec la pomme
        if new_head == apple:
            apple = (random.randint(0, (width - block_size) // block_size) * block_size,
                     random.randint(0, (height - block_size) // block_size) * block_size)
        else:
            snake.pop()

    # Effacement de l'écran
    screen.fill(black)

    # Affichage de la pomme
    pygame.draw.rect(screen, red, (apple[0], apple[1], block_size, block_size))

    # Affichage du serpent
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], block_size, block_size))

    # Affichage du bouton "Quit" uniquement (issue 3)
    font = pygame.font.Font(None, 36)
    quit_button = font.render("Quit", True, quit_button_color)
    pygame.draw.rect(screen, black, quit_button_rect)
    screen.blit(quit_button, (width - quit_button.get_width() - 10, 10))

    # Affichage du texte "Press Enter to begin" si le jeu est en pause (issue 3)
    if not running and show_start_text:
        start_text = font.render("Press the touch space to begin", True, white)
        text_x = width // 2 - start_text.get_width() // 2
        text_y = height // 3 - start_text.get_height() // 2  
        screen.blit(start_text, (text_x, text_y))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Régulation de la vitesse du serpent
    pygame.time.Clock().tick(speed)
