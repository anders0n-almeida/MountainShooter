import pygame

from game_code.Entity import Entity
from game_code.Consts import *

class Player(Entity):

    def __init__(self, name: str, entity_type: str, position: tuple):

        super().__init__(name, entity_type, position)

    def move(self):
        
        # o método utilizado para definir o movimento do jogador precisa ser o '.key.get_pressed()' pois ele prevê um efeito contínuo (manter a tecla pressionada gera um efeito prolongado, diferente da opção escolhida para movimentar entre as opções do menu, por exemplo)
        pressed_key = pygame.key.get_pressed()

        # LEMBRE-SE!
        # O ponto (0, 0) da tela se encontra no CANTO SUPERIOR ESQUERDO
        # Isso significa que mover o jogador para CIMA significa reduzir a sua posição do eixo Y

        # Movimentar o jogador para CIMA enquanto ele não atingir o topo da tela (self.rect.top > 0)
        # TECLA W
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Movimentar o jogador para BAIXO enquanto ele não atingir o fundo da tela (self.rect.bottom < WIN_HEIGHT)
        # TECLA S
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Movimentar o jogador para ESQUERDA enquanto ele não atingir a borda esquerda da tela (self.rect.left > 0)
        # TECLA A
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimentar o jogador para DIREITA enquanto ele não atingir a borda direita da tela (self.rect.right < WIN_WIDTH)
        # TECLA D
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]