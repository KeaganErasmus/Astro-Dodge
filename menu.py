import pygame

class Menu:
    def __init__(self) -> None:
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 32)
        self.font = pygame.font.Font(None, 20)

        self.title_rec = ""
        self.play_text = pygame.Rect
        self.quit_text = pygame.Rect


    def draw_menu(self, screen):
        title_text = self.title_font.render("Astro Dodge", True, "White")
        play_text = self.font.render("Play", True, "White")
        quit_text = self.font.render("Quit", True, "White")

        self.title_rec = title_text.get_rect()
        self.play_rec = title_text.get_rect()
        self.quit_rec = title_text.get_rect()

        screen.blit(title_text, ((screen.get_width() // 2 - 50), 100))
        screen.blit(play_text, (400, 150))
        screen.blit(quit_text, (400, 200))

        pygame.draw.rect(screen, "green", self.title_rec)
    
    def clicked_button(self):
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.title_rec.collidepoint(mouse):
                    print("title")