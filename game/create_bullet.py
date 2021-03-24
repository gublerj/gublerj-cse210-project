import arcade

class create_bullet(arcade.Sprite):

    def __init__(self, sprite, scalling):
        super().__init__(sprite, scalling)
        self.fire = False

    def fire(self):
        self.fire = True

    def cease_fire(self):
        self.fire = False

    def update(self)