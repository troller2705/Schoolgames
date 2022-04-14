import pygame
import sys

sys.path.append('./Games/P')
sys.path.append('./Games/SA')
sys.path.append('./Games/AQ')
import platformer
import shark_attack
import ancient_quest


class Menu:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.display.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_cross(self):
        for y_offset in range(0, 100, 10):
            pygame.draw.line(self.game.display, self.game.RED,
                             [0, 0 + y_offset], [self.x, self.y + y_offset], 2)
            pygame.draw.line(self.game.display, self.game.RED,
                             [0, self.y + y_offset], [self.x, 0 + y_offset], 2)
        # pygame.draw.polygon(self.game.display, self.game.RED,
        #   [[self.mid_w, self.mid_h], [340, 345], [400, 390], [460, 345]], 0)

    def draw_characters(self):
        sharkS = pygame.image.load('Games/SA/Characters/Shark.R.png')
        platformerS = pygame.image.load('Games/P/Characters/Platformer.png')
        adventurerS = pygame.image.load('Games/AQ/Characters/Adventurer.png')
        self.game.display.blit(sharkS, (self.mid_w / 6, self.mid_h - 50))
        self.game.display.blit(platformerS, (self.mid_w - 85, self.mid_h - 230))
        self.game.display.blit(adventurerS, (self.mid_w + 200, self.mid_h - 50))


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 200
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 225
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 250
        self.exitx, self.exity = self.mid_w, self.mid_h + 275
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # double quotes for use of apostrophe
            self.game.draw_text("Troller's Paradise", 30, self.mid_w, self.mid_h - 250)
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Exit', 20, self.exitx, self.exity)
            self.draw_cross()
            self.draw_cursor()
            self.draw_characters()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + -70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + -70, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + -40, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + -40, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + -70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + -70, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.game_menu
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Exit':
                pygame.quit()

            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 225
        self.videox, self.videoy = self.mid_w, self.mid_h + 250
        self.cursor_rect.midtop = (self.volx + -60, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Volume', 20, self.volx, self.voly)
            self.game.draw_text('Controls', 20, self.controlsx, self.controlsy)
            self.game.draw_text('Video', 20, self.videox, self.videoy)
            self.draw_cross()
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.controlsx + -80, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.videox + -50, self.videoy)
                self.state = 'Video'
            elif self.state == 'Video':
                self.cursor_rect.midtop = (self.volx + -60, self.voly)
                self.state = 'Volume'
        elif self.game.UP_KEY:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.videox + -50, self.videoy)
                self.state = 'Video'
            elif self.state == 'Video':
                self.cursor_rect.midtop = (self.controlsx + -80, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.volx + -60, self.voly)
                self.state = 'Volume'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume_menu
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.controls_menu
            elif self.state == 'Video':
                self.game.curr_menu = self.game.video_menu

            self.run_display = False


class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume Mute'
        self.volx, self.voly = self.mid_w, self.mid_h + 225
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 250
        self.cursor_rect.midtop = (self.volx + -85, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Volume', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text(f'Mute:{self.game.mute}', 20, self.volx, self.voly)
            self.draw_cross()
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Volume Mute' and self.game.mute == 'Off':
                pygame.mixer.pause()
                self.game.mute = 'On'
            elif self.state == 'Volume Mute' and self.game.mute == 'On':
                pygame.mixer.unpause()
                self.game.mute = 'Off'


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.volx, self.voly = self.mid_w, self.mid_h + 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 225
        self.videox, self.videoy = self.mid_w, self.mid_h + 250

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Controls', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Arrow Keys', 20, self.volx, self.voly)
            self.game.draw_text('Enter', 20, self.controlsx, self.controlsy)
            self.game.draw_text('Backspace', 20, self.videox, self.videoy)
            self.draw_cross()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False


class VideoMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Video Mode'
        self.n = 0
        self.volx, self.voly = self.mid_w, self.mid_h + 225
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 250
        self.cursor_rect.midtop = (self.volx + -155, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Video', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text(f'Mode:{self.game.VideoMode}', 20, self.volx, self.voly)
            self.draw_cross()
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Video Mode' and self.game.VideoMode == 'Windowed':
                self.game.VideoMode = 'Fullscreen'
                self.game.mode = pygame.FULLSCREEN
                self.game.display.blit
            elif self.state == 'Video Mode' and self.game.VideoMode == 'Fullscreen':
                self.game.VideoMode = 'Windowed'
                self.game.mode = pygame.RESIZABLE
                self.game.display.blit


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 40, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Made by Deathboard Productions', 25, self.mid_w, self.mid_h - 100)
            self.game.draw_text('Lead Developer, Graphics Designer, Sound Engineer:', 15, self.mid_w, self.mid_h + 25)
            self.game.draw_text('Troller AKA Cole', 25, self.mid_w, self.mid_h + 50)

            self.blit_screen()


class GameMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.playing = False
        self.state = 'Ancient Quest'
        self.g1x, self.g1y = self.mid_w, self.mid_h + 225
        self.g2x, self.g2y = self.mid_w, self.mid_h + 250
        self.g3x, self.g3y = self.mid_w, self.mid_h + 275
        self.cursor_rect.midtop = (self.g1x + -135, self.g1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Game Selections', 30, self.mid_w, self.mid_h - 250)
            self.game.draw_text('Ancient Quest', 20, self.g1x, self.g1y)
            self.game.draw_text('Platformer', 20, self.g2x, self.g2y)
            self.game.draw_text('Shark Attack', 20, self.g3x, self.g3y)
            self.draw_cross()
            self.draw_cursor()
            self.draw_characters()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Ancient Quest':
                self.cursor_rect.midtop = (self.g2x + -105, self.g2y)
                self.state = 'Platformer'
            elif self.state == 'Platformer':
                self.cursor_rect.midtop = (self.g3x + -125, self.g3y)
                self.state = 'Shark Attack'
            elif self.state == 'Shark Attack':
                self.cursor_rect.midtop = (self.g1x + -135, self.g1y)
                self.state = 'Ancient Quest'
        elif self.game.UP_KEY:
            if self.state == 'Ancient Quest':
                self.cursor_rect.midtop = (self.g3x + -125, self.g3y)
                self.state = 'Shark Attack'
            elif self.state == 'Platformer':
                self.cursor_rect.midtop = (self.g1x + -135, self.g1y)
                self.state = 'Ancient Quest'
            elif self.state == 'Shark Attack':
                self.cursor_rect.midtop = (self.g2x + -105, self.g2y)
                self.state = 'Platformer'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Ancient Quest':
                self.playing = True
                ancient_quest.AncientQuest.game_loop(self)
            elif self.state == 'Platformer':
                self.playing = True
                platformer.Platformer.game_loop(self)
            elif self.state == 'Shark Attack':
                self.playing = True
                shark_attack.SharkAttack.game_loop(self)

    def draw_characters(self):
        sharkS = pygame.image.load('Games/SA/Characters/Shark.R.png')
        platformerS = pygame.image.load('Games/P/Characters/Platformer.png')
        adventurerS = pygame.image.load('Games/AQ/Characters/Adventurer.png')
        if self.state == 'Ancient Quest':
            self.game.display.blit(adventurerS, (self.mid_w - 85, self.mid_h - 230))
        elif self.state == 'Shark Attack':
            self.game.display.blit(sharkS, (self.mid_w - 85, self.mid_h - 230))
        elif self.state == 'Platformer':
            self.game.display.blit(platformerS, (self.mid_w - 85, self.mid_h - 230))


pygame.display.quit()
pygame.quit()
