import arcade

class Input_service:
    
    def __init__(self):
        #self.player_sprites = player_sprites["player"][0]
        pass

    def on_release(self, key, modifiers, player_sprites):
        player_sprite = player_sprites["player"][0][0]
        if key == arcade.key.UP or key == arcade.key.W:
            player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            player_sprite.change_x = 0
        return player_sprite