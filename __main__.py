import random
from game import constants
from game.director import Director
from game.zombie import create_zombie
import arcade

# Setup window
director = Director(constants.MAX_X, constants.MAX_Y, constants.SCREEN_TITLE)

test = zombie()
# Start game
director.start_game()