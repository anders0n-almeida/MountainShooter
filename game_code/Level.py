import pygame

from game_code.Entity import Entity
from game_code.EntityFactory import EntityFactory

class Level:

    def __init__(self, window: pygame.surface.Surface, level_name: str, game_mode):

        self.window = window
        self.level_name = level_name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):

        while True:

            for entity in self.entity_list:
                self.window.blit(source = entity.surf, dest = entity.rect)
                entity.move()
            pygame.display.flip()
            