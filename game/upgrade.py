import arcade
from game import constants

class Upgrade(arcade.Sprite):

    def __init__(self, sprite, scaling, name):
        super().__init__(sprite, scaling)
        self.name = name

    def get_name(self):
        return self.name

    