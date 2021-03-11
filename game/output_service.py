import sys
from game import constants
import arcade

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        pass
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        arcade.draw_text(text, x, y, arcade.color.SKY_BLUE)

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)