from game_code.Entity import Entity
from game_code.Consts import *

class Background(Entity):

    def __init__(self, name: str, entity_type: str, position: tuple):

        super().__init__(name, entity_type, position)

    def move(self):

        # movendo o background para a esquerda (direção contrária a qual o jogador se move)
        # negativo no eixo x
        # a instrução abaixo define a VELOCIDADE de movimentação do background
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # quando a ponta direita da imagem chegar no ponto zero ou tiver valor negativo, significa que ele se moveu totalmente para a esquerda
        # quando isso ocorrer, devemos capturar a posição da esquerda e transportar para o canto direito
        # desse forma, geramos um loop de apresentação de imagens
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH