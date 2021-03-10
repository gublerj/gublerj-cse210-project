import arcade

class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        # Setup the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SPACE_CADET)
        self.set_update_rate(1/30)
         # create the cast {key: tag, value: list}
        cast = {}

        script["input"] =  []
        script["update"] = []
        script["output"] = []

        self._cast = cast
        self._script = script

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        arcade.run()


    def on_update(self, delta_time: float):
        self._cue_action("input")
        self._cue_action("update")


    def on_draw(self):
        arcade.start_render()
        self._cue_action("output")


    def on_key_press(self, symbol, modifiers):
        pass


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)