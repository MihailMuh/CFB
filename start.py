import sys
from file_manager import *
from colors import *
from windows import WIDTH, HEIGHT


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    image = load_image("preview_screen.jpg", (WIDTH, HEIGHT))
    screen.blit(image, (0, 0))
    string_rendered = pygame.font.Font(None, 50).render("Для продолжения нажмите любую клавишу", True,
                                                        pygame.Color('dark blue'))
    intro_rect = string_rendered.get_rect()
    intro_rect.y = 700
    intro_rect.x = 300
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


class Start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 50))
        self.image.fill(PowderBlue)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH * 3 / 4, HEIGHT / 2)

    def update(self):
        pass


screen = pygame.display.set_mode((WIDTH, HEIGHT),
                                 pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=True)

all_sprites = pygame.sprite.Group()
start = Start()
all_sprites.add(start)

running = True
number = 0

start_screen()

game_screen = load_image("game_screen.jpg", (WIDTH, HEIGHT))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    # screen.fill(LightSteelBlue)
    screen.blit(game_screen, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    pygame.display.update()

terminate()
