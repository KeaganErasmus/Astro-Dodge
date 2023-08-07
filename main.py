import pygame
import random

from player import Player
from astroid import Astroid

game_state = "game"

def main_game(screen, dt, player, ships):
        # PLayer Related Methods
        player.draw_player(screen)
        player.update(dt)

        # Enemy Related Methods
        for ship in ships:
            ship.draw_ship()
            ship.update(dt)

def main_menu():
    pass

def game_lost():
    pass

def main():
    pygame.init()
    pygame.display.set_caption("Space Shooter")
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()

    player = Player("assets/player_ship.png", 16, 16, 400, 300, 500)

    astroids = []
    max_astroids = 10

    for i in range(max_astroids):
        new_astroid = Astroid("assets/enemy_ship.png", 16, 16, random.randrange(0, screen.get_width()), random.randrange(0,50), random.randrange(250,300), screen)
        astroids.append(new_astroid)

    running = True
    while running:
        dt = clock.tick() / 1000
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Depending on what state the game is in run the corrisponding methods
        if game_state == "game":
            main_game(screen, dt, player, astroids)
        if game_state == "lost":
            game_lost()
        if game_state == "menu":
            main_menu()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()