from game_code.Entity import Entity
from game_code.Consts import *

class PlayerShot(Entity):

    def __init__(self, name: str, entity_type: str, position: tuple):

        super().__init__(name, entity_type, position)

    def move(self):

        self.rect.centerx += ENTITY_SPEED[self.name]