from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this
    class of objects is to draw all actors in the cast.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors. The action in this
        case is to draw each actor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                self._output_service.draw_actor(actor)