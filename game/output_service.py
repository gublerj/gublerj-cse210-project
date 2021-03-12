import arcade

class Output_service:

    def __init__(self):
        pass

    def execute(self, actor, actors):
        actor.draw()
        actors.draw()
