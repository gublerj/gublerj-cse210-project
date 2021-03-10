import random
from game import constants
from game.director import Director
import arcade

# Setup window
director = Director(constants.MAX_X, constants.MAX_Y, constants.SCREEN_TITLE)

# Start game
director.start_game()