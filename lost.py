import pygame

class Lost:
    def __init__(self) -> None:
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 32)
        self.font = pygame.font.Font(None, 20)

        self.title_rec = ""
        self.play_text = pygame.Rect(400,150, 26, 20)
        self.quit_text = pygame.Rect


    def draw_menu(self, screen):
        title_text = self.title_font.render("You Lost :(", True, "White")
        play_text = self.font.render("Play", True, "White")
        quit_text = self.font.render("Quit", True, "White")
    

        self.quit_rec = quit_text.get_rect()
        self.quit_rec.center = ((screen.get_width() // 2 + 15), 205)

        screen.blit(title_text, ((screen.get_width() // 2 - 50), 100))
        screen.blit(play_text, (400, 150))
        screen.blit(quit_text, (400, 200))

    
    def clicked_button(self) -> str:
        button_pressed = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if button_pressed[0]:
            if self.play_text.collidepoint(mouse):
                print("play")
                return "play"
            if self.quit_rec.collidepoint(mouse):
                print("quit")
                return "quit"