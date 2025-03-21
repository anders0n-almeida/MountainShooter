from abc import ABC, abstractmethod
import pygame.image

from game_code.Consts import *

class Entity(ABC):

    def __init__(self, name: str, entity_type: str, position: tuple):

        self.name = name
        self.entity_type = entity_type
        self.position = position
        self.surf = pygame.image.load('./assets/' + self.entity_type + "/" + self.name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name] if self.name in ENTITY_HEALTH.keys() else None

        @abstractmethod
        def move(self):
            ...