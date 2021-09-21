import system
from file_manager import *
from button import Button
from windows import *
from font import Font
from statuses import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN |
                                              pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=True)

        self.all_sprites = pygame.sprite.Group()
        self.font = None
        self.background_screen = None
        self.button = None

        self.running = True
        self.game_status = PASS

    def start_screen(self):
        self.font.render()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    system.terminate()
                else:
                    self.generate_game()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.button.click(pos[0], pos[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    system.terminate()

    def generate_menu(self):
        self.font = Font(self.screen, 70, "Для продолжения нажмите любую клавишу", HALF_SCREEN_WIDTH,
                         SCREEN_HEIGHT - 100,
                         pygame.Color('dark blue'))
        self.background_screen = load_image("preview_screen.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.game_status = PREVIEW

    def generate_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.button = Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)
        self.all_sprites.add(self.button)

        self.background_screen = load_image("game_screen.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.game_status = GAME

    def run(self):
        while self.running:
            self.screen.blit(self.background_screen, (0, 0))

            if self.game_status == PREVIEW:
                self.start_screen()
            elif self.game_status == GAME:
                self.main_game()

            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            pygame.display.flip()


game = Game()
game.generate_menu()
game.run()