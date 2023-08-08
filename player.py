import pygame

class Player:
    def __init__(self, sprite: str, width: int, height: int, x: int, y: int, speed: int) -> None:
        self.sprite = pygame.image.load((sprite))
        self.width  = width
        self.height = height
        self.pos_x  = x
        self.pos_y  = y
        self.speed  = speed

        self.player_rec = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def draw_player(self, display: pygame.Surface) -> pygame.Surface:
        display.blit(self.sprite, (self.pos_x, self.pos_y))

    def update(self, dt) -> None:
        self.player_rec = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos_x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos_x += self.speed * dt
        if keys[pygame.K_w]:
            self.pos_y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos_y += self.speed * dt

    def collisions(self, astroids):
        if self.player_rec.collidelistall(astroids):
            print("hit")