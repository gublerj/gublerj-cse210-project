import arcade

class Output_service:

    def __init__(self):
        pass

    def execute(self, actors):
        player = actors['player'][0][0]
        zombies = actors['zombie'][0]
        bullets = actors['bullet'][0]
        player.draw()
        for zombie in zombies:
            zombie.draw()
        for bullet in bullets:
            bullet.draw()
        
        arcade.draw_text(f"Health: {player.get_health()}", 10, 20, arcade.color.WHITE, 14)