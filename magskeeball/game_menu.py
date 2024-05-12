from .state import State, GameMode
from . import constants as const
import random


class GameMenu(GameMode):

    def startup(self):
        self.refresh_game_modes()
        self.ticks = 0
        self.locked = False
        self.lock_time = 9999999
        self.showing_hidden_games = False
    
    def refresh_game_modes(self, modes=None):
        if not modes:
            modes = self.manager.game_modes
        self.game_modes = modes
        self.game_position = len(self.game_modes) - 1
        self.next_game()

    def handle_event(self, event):
        if event.button == const.B.QUIT:
            self.quit = True
        if not self.locked:
            if event.button == const.B.SELECT and event.down:
                self.next_game()
            if event.button == const.B.START and event.down:
                self.manager.next_state = self.mode_name
                self.persist["active_game_mode"] = self.mode_name
                self.locked = True
                self.lock_time = self.ticks
                if self.mode_name == "TARGET":
                    self.start_song = self.res.sounds['target']["TARGET_INTRO"]
                else:
                    self.start_song = random.choice(
                        list(self.res.sounds['start'].values())
                    )
                self.start_song.play()
        else:
            if event.button in [const.B.START, const.B.SELECT] and event.down:
                self.done = True

    def update(self):
        self.ticks += 1
        if self.ticks > self.lock_time + 3 * const.FPS:
            self.done = True

    def draw_panel(self, panel):
        panel.clear()
        title = "{} MODE".format(self.mode_name)
        x = 48 - 3 * len(title)
        panel.draw_text((x, 1), title, "Medium", "PURPLE")
        for i, line in enumerate(self.intro_text):
            panel.draw_text((1, 13 + 8 * i), line, "Small", "YELLOW")
        if not self.locked:
            panel.draw_text((20, 49), "SELECT MODE", "Small", "WHITE")
            if self.ticks % (3 * const.FPS) < 1.5 * const.FPS:
                panel.draw_text((10, 56), "YELLOW = CHANGE", "Small", "WHITE")
            else:
                panel.draw_text((20, 56), "RED = START", "Small", "WHITE")

    def next_game(self):
        self.game_position = (self.game_position + 1) % len(self.game_modes)
        self.mode_name = self.game_modes[self.game_position]
        self.mode = self.manager.states[self.mode_name]
        self.intro_text = self.mode.intro_text
        print("Switching to mode {} {}".format(self.game_position, self.mode_name))
