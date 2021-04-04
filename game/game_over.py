import arcade
from game import constants
class GameOverView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        WIDTH = constants.SCREEN_WIDTH
        HEIGHT = constants.SCREEN_HEIGHT
        TITLE = constants.SCREEN_TITLE
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH / 2, arcade.color.WHITE, 54)

        time_taken_formatted = f"{round(self.score, 2)} points"
        arcade.draw_text(f"Final Score: {time_taken_formatted}",
                         WIDTH/2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        #output_total = f"Total Score: {self.window.total_score}"
        #arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        pass