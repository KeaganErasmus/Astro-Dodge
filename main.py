import pygame
import random
import time

from player import Player
from astroid import Astroid
from score import Score
from menu import Menu
from lost import Lost

screen = pygame.display.set_mode((800, 400))

game_state = "menu"
old_time = time.time()

menu = Menu()
lost = Lost()

score = 0
score = Score(score)

player = Player("assets/player_ship.png", 16, 16, 400, 300, 500)
player_rec = player.player_rec

astroids = []
max_astroids = 10

for i in range(max_astroids):
    new_astroid = Astroid("assets/enemy_ship.png", 16, 16, random.randrange(0, screen.get_width()), random.randrange(0,50), random.randrange(250,300), screen)
    astroids.append(new_astroid)


def main_game(screen, dt, player, astroids):
    global game_state
    # PLayer Related Methods
    player.draw_player(screen)
    player.update(dt)
    
    # rec_list = list(map(lambda x: x.get_rec(), astroids))
    rec_list = [astroid.get_rec() for astroid in astroids]

    # Score Related Methods
    score.draw_score(screen)
    score.update_score()

    # Enemy Related Methods
    for astroid in astroids:
        astroid.draw_ship()
        astroid.update(dt)
    
    if player.collisions(rec_list):
        game_state = "lost"


def main_menu():
    global game_state
    menu.draw_menu(screen)
    if menu.clicked_button() == "play":
        game_state = "game"
    elif menu.clicked_button() == "quit":
        pygame.quit()


def game_lost(screen):
    global game_state
    lost.draw_menu(screen)
    if lost.clicked_button() == "play":
        game_state = "game"
    elif lost.clicked_button() == "quit":
        pygame.quit()



def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    running = True
    while running:       
        dt = clock.tick() / 1000
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Depending on what state the game is in run the corrisponding methods
        if game_state == "menu":
            main_menu()
        elif game_state == "game":
            main_game(screen, dt, player, astroids)
        elif game_state == "lost":
            game_lost(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()