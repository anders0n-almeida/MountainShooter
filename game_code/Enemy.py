from game_code.EnemyShot import EnemyShot
from game_code.Entity import Entity
from game_code.Consts import *

class Enemy(Entity):

    def __init__(self, name: str, entity_type: str, position: tuple):

        super().__init__(name, entity_type, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # Atributos específicos do Player, necessários para o efeito de "piscar" vermelho ao receber dano
        self.original_image = self.surf.copy()  # Armazena a imagem original
        self.is_damaged = False
        self.damage_timer = 0

    def move(self):

        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self) -> EnemyShot:

        self.shot_delay -= 1

        if self.shot_delay == 0:

            # Renovando o atraso/delay do tiro para o valor inicial
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            return EnemyShot(f'{self.name}Shot', 'particles', (self.rect.centerx, self.rect.centery))