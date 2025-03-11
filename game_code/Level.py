import pygame

from game_code.Entity import Entity

class Level:

    def __init__(self, window: pygame.surface.Surface, level_name: str, game_mode):

        self.window = window
        self.level_name = level_name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

    def run():

        ...