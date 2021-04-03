import arcade
from game import constants

class Upgrade(arcade.Sprite):

    def __init__(self, sprite, scaling, name):
        """This class stores the upgrade 
        and the name of the upgrade so that we can better use it
        """
        super().__init__(sprite, scaling)
        self.name = name

    def get_name(self):
        return self.name

    