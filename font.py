from pygame_init import *


class Font:
    def __init__(self, screen, size, text, x, y, color=pygame.Color("black")):
        self.screen = screen
        self.string = pygame.font.Font(None, size).render(text, True, color)
        rect = self.string.get_rect()
        self.pos = (x - (rect.width / 2), y - (rect.height / 2))

    def render(self):
        self.screen.blit(self.string, self.pos)
