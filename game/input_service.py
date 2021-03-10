import sys
from game.point import Point
import arcade

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._symbol = ""
        self._modifiers = ""
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(10, 0)

        if self._symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if self._symbol == arcade.key.A or self._symbol == arcade.key.LEFT:
            direction = Point(-10, 0)

        if self._symbol == arcade.key.D or self._symbol == arcade.key.RIGHT:
            direction = Point(10, 0)

        return direction


    def set_symbols(self, symbol, modifiers):
        self._symbol = symbol
        self._modifiers = modifiers
