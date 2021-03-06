from assets.scripts import system
from assets.scripts.file_manager import *
from assets.scripts.button import Button
from assets.scripts.windows import *
from assets.scripts.font import Font
from assets.scripts.statuses import *
from assets.scripts.chemical_elements import chemical_elements


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN |
                                              pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=True)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.background_screen = None
        self.button = None

        self.font = None
        self.fps_font = Font(self.screen, 30, "", SCREEN_WIDTH - 200, 50,
                             pygame.Color('red'))

        self.running = True
        self.draw_fps = False
        self.game_status = PASS

    def start_screen(self):
        self.font.render()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                else:
                    self.generate_game()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for button in self.all_sprites:
                    button.click(pos[0], pos[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break

    def generate_menu(self):
        self.font = Font(self.screen, 70, "Для продолжения нажмите любую клавишу", HALF_SCREEN_WIDTH,
                         SCREEN_HEIGHT - 100,
                         pygame.Color('dark blue'))
        self.background_screen = load_image("preview_screen.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.game_status = PREVIEW

    def generate_game(self):
        self.all_sprites = pygame.sprite.Group()
        x = 10
        y = 10
        width = 130
        height = 60
        step_x = width + x
        step_y = height + y
        end_x = SCREEN_WIDTH - step_x
        keys = chemical_elements.keys()

        for k in keys:
            self.all_sprites.add(Button(x, y, load_image("elements/" + k + ".jpg", (width, height))))

            x += step_x
            if x >= end_x:
                x = 10
                y += step_y

        self.font = None

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

            if self.draw_fps:
                self.fps_font.render('FPS:' + str(int(self.clock.get_fps())))
                self.clock.tick(-1)

            pygame.display.flip()

        system.terminate()


game = Game()
game.generate_menu()
game.run()
