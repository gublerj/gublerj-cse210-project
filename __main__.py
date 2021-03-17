from game.director import Director
from game.main_menu import main_menu
from game import constants
import arcade
#window = Director()
#window.execute()

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_TITLE = constants.SCREEN_TITLE

window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
start_view = main_menu()
window.show_view(start_view)
#start_view.setup()
arcade.run()