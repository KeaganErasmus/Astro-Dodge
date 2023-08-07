import pygame, time

class Score:
    def __init__(self, score) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(None, 32)
        self.score = score
        self.old_time = time.time()
    
    def draw_score(self, screen):
        score_text = self.font.render(f'{self.score}', True, "white")
        screen.blit(score_text, (400, 200))

    def update_score(self):
        current_time = time.time()
        if current_time - self.old_time >= 3:
            self.score += 1
            self.old_time = current_time