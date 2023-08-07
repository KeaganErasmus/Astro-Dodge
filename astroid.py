import pygame, random

class Astroid:
    def __init__(self, sprite: str, width: int, height: int, x: int, y: int, speed: int, screen: pygame.Surface) -> None:
        self.sprite = pygame.image.load((sprite))
        self.width  = width
        self.height = height
        self.pos_x  = x
        self.pos_y  = y
        self.speed  = speed
        self.screen = screen

        self.enemy_rec = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        self.direction = "right"

    def draw_ship(self) -> pygame.Surface:
        self.screen.blit(self.sprite, (self.pos_x, self.pos_y))

    def update(self, dt) -> None:
        self.enemy_rec = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        self.pos_y += self.speed * dt

        if self.direction == "right":
            self.pos_x += self.speed * dt
        if self.direction == "left":
            self.pos_x -= self.speed * dt

        if self.pos_x >= self.screen.get_width() - self.width:
            self.direction = "left"
        if self.pos_x <= 0:
            self.direction = "right"

        if self.pos_y >= self.screen.get_height():
            self.pos_y = 0


