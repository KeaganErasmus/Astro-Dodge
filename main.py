import pygame
import random
import time

from player import Player
from astroid import Astroid
from score import Score

screen = pygame.display.set_mode((800, 400))

game_state = "game"
old_time = time.time()

score = 0

score = Score(score)
player = Player("assets/player_ship.png", 16, 16, 400, 300, 500)
player_rec = player.player_rec

astroids = []
astroid_rects = []
max_astroids = 10

for i in range(max_astroids):
    new_astroid = Astroid("assets/enemy_ship.png", 16, 16, random.randrange(0, screen.get_width()), random.randrange(0,50), random.randrange(250,300), screen)
    astroids.append(new_astroid)


def main_game(screen, dt, player, astroids):
    # PLayer Related Methods
    player.draw_player(screen)
    player.update(dt)
    
    rec_list = list(map(lambda x: x.get_rec(), astroids))

    # Score Related Methods
    score.draw_score(screen)
    score.update_score()

    # Enemy Related Methods
    for astroid in astroids:
        astroid.draw_ship()
        astroid.update(dt)
    
    player.collisions(rec_list)


def main_menu():
    pass


def game_lost():
    pass


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    
    # print(astroid_rects)
    # print(player_rec)

    running = True
    while running:
        dt = clock.tick() / 1000
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # for rects in astroid_rects:
        #     pygame.draw.rect(screen, "green", rects)
        
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