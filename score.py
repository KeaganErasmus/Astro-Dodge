import pygame

class Score:
    def __init__(self) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(None, 32)
        self.score = 0

    def draw_score(self, screen):
        score_text = self.font.render(f'{self.score}', True, "white")
        screen.blit(score_text, (400, 200))

    def update_score(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.score += 1
        print(self.score)