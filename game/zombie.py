from game.actor import Actor

class create_zombie(Actor):

    def __init__(self, position, sprite = "\env\Lib\site-packages\arcade\resources\images\animated_characters\zombie\zombie_walk0.png"):
        zombie = Actor()
        self._sprite = sprite
        self._position = position
        zombie.set_sprite(self._sprite)
        zombie.set_position(self._position)