import pygame

class Menu:
    def __init__(self) -> None:
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 32)
        self.font = pygame.font.Font(None, 20)


    def draw_menu(self, screen):
        title_text = self.title_font.render("Astro Dodge", True, "White")
        play_text = self.font.render("Play", True, "White")
        quit_text = self.font.render("Quit", True, "White")

        screen.blit(title_text, ((screen.get_width() // 2 - 50), 100))
        screen.blit(play_text, (400, 150))
        screen.blit(quit_text, (400, 200))