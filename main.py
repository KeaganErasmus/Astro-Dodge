import pygame
import random
import time

from player import Player
from asteroid import Asteroid
from score import Score
from menu import Menu
from lost import Lost

screen = pygame.display.set_mode((800, 400))

game_state = "menu"
running = True
old_time = time.time()

menu = Menu()
lost = Lost()

score = 0
score = Score(score)

player = Player("assets/player_ship.png", 16, 16, 400, 300, 500)
player_rec = player.player_rec

asteroids = []
max_asteroids = 10

for i in range(max_asteroids):
    new_asteroid = Asteroid("assets/enemy_ship.png", 16, 16, random.randrange(0, screen.get_width()),
                          random.randrange(0, 50), random.randrange(250, 300), screen)
    asteroids.append(new_asteroid)


def main_game(screen, dt, player, asteroids):
    global game_state
    # PLayer Related Methods
    player.draw_player(screen)
    player.update(dt)

    # rec_list = list(map(lambda x: x.get_rec(), asteroids))
    rec_list = [asteroid.get_rec() for asteroid in asteroids]

    # Score Related Methods
    score.draw_score(screen)
    score.update_score()

    # Enemy Related Methods
    for asteroid in asteroids:
        asteroid.draw_ship()
        asteroid.update(dt)

    if player.collisions(rec_list):
        game_state = "lost"


def main_menu():
    global game_state, running
    menu.draw_menu(screen)
    if menu.clicked_button() == "play":
        game_state = "game"
    elif menu.clicked_button() == "quit":
        running = False


def game_lost(screen):
    global game_state, running
    lost.draw_menu(screen)
    if lost.clicked_button() == "menu":
        game_state = "menu"
    elif lost.clicked_button() == "quit":
        running = False


def main():
    global running
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    # running = True
    while running:
        dt = clock.tick() / 1000
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Depending on what state the game is in run the corresponding methods
        if game_state == "menu":
            main_menu()
        elif game_state == "game":
            main_game(screen, dt, player, asteroids)
        elif game_state == "lost":
            game_lost(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
