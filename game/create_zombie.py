from game.actor import Actor
from game.point import Point
from game import constants

class Create_zombie(Actor):
    """This class will allow us to create basic zombies with ease"""

    def __init__(self):
        super().__init__()
        self.set_sprite(":resources:images/animated_characters/zombie/zombie_idle.png")
        self.set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT))