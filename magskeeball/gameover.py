from .state import State
from . import resources as res


class GameOver(State):

    def startup(self):
        self.ticks = 0
        self.game_modes = self.manager.game_modes
        self.red_game = self.settings["red_game"]
        self.yellow_game = self.settings["yellow_game"]

    def handle_event(self, event):
        if event.button == res.B.START and event.down:
            self.activate_new_mode(self.red_game)
        elif event.button == res.B.SELECT and event.down:
            self.activate_new_mode(self.yellow_game)

        elif event.button == res.B.CONFIG and event.down:
            self.activate_new_mode("ATTRACT")

    def activate_new_mode(self, mode):
        if mode in self.game_modes:
            self.manager.next_state = "INTRO"
            self.persist["active_game_mode"] = mode
        else:
            self.manager.next_state = mode
        self.done = True

    def update(self):
        self.ticks += 1
        if self.ticks >= res.FPS * 5:
            self.manager.next_state = "ATTRACT"
            self.done = True

    def draw_panel(self, panel):
        panel.clear()
        panel.draw_text((3, 34), "GAME OVER", "MAGMini", "RED")

        if self.manager.states[self.persist["active_game_mode"]].is_speed_game:
            display_time = self.persist["last_score"]

            panel.draw_time((7, 6), display_time, 'YELLOW')

        else:
            score = self.persist["last_score"]
            score_x = 17 if score < 10000 else 4
            panel.draw_text((score_x, 4), f"{score:04d}", "Digital16", "YELLOW")

        if self.ticks % (2 * res.FPS) < (1.5 * res.FPS):
            panel.draw_text((15, 54), "PRESS START", "Medium", "WHITE")
