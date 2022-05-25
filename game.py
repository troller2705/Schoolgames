import pygame

from menu import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False
        self.DISPLAY_W = pygame.display.get_desktop_sizes()[0][0]
        self.DISPLAY_H = pygame.display.get_desktop_sizes()[0][1]
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.display = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.FULLSCREEN)
        Menu_icon = pygame.image.load('UI/icon.png')
        pygame.display.set_icon(Menu_icon)
        pygame.display.set_caption("Troller's Paradise")
        self.clock = pygame.time.Clock()
        self.font_name = 'UI/8-Bit.ttf'
        self.BLACK, self.WHITE, self.GREEN, self.RED = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.game_menu = GameMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.controls_menu = ControlsMenu(self)
        self.curr_menu = self.main_menu
        self.mute1 = 'On'
        self.mute2 = 'On'
        pygame.mixer.music.load('Music&Sounds/Menu/8_Bit_Menu.mp3')
        pygame.mixer.music.play(-1)
        self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
