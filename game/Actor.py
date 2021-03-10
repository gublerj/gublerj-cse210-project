from game import constants
from game.point import Point

#Change the sprittual to what makes more sense
class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _tag (string): The actor's tag.
        _sprit (string): The spritual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._description = ""
        self._sprit = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_description(self):
        """Gets the artifact's description.
        
        Returns:
            string: The artifact's description.
        """
        return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_sprit(self):
        """Gets the actor's spritual representation.
        
        Returns:
            string: The actor's spritual representation.
        """
        return self._sprit

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_sprit(self, sprit):
        """Updates the actor's sprit to the given value.
        
        Args:
            sprit (string): The given value.
        """
        self._sprit = sprit

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def collision(self, other):
        """Return True if this object and other occupy the
        same space."""
        other_x = other.get_position().get_x()
        other_y = other.get_position().get_y()
        self_x = self.get_position().get_x()
        self_y = self.get_position().get_y()

        return ((self_y in range(other_y - 5, other_y + 5) 
                 or 
                 other_y in range(self_y - 5, self_y + 5))
             and 
                (self_x in range(other_x, other_x + 10 * len(other.get_sprit())) or
                 other_x in range(self_x, self_x + 10 * len(self.get_sprit()))
                )
        )