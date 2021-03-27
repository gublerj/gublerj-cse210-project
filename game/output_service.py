import arcade

class Output_service:

    def __init__(self):
        pass

    def execute(self, actors):
        player = actors['player'][0][0]
        zombies = actors['zombie'][0]
        bullets = actors['bullet'][0]
        walls = actors['wall'][0]
        obsticals = actors['obsticals'][0]
        #weapon = actors['weapon'][0][0]

        #weapon.draw()
        player.draw()
        for zombie in zombies:
            zombie.draw()
        for bullet in bullets:
            bullet.draw()
        for wall in walls:
            wall.draw() 
        for obstical in obsticals:
            obstical.draw()
        
        arcade.draw_text(f"Health: {player.get_health()}", 10, 20, arcade.color.WHITE, 14)