from random import randint

from game_code.Consts import *
from game_code.Background import Background
from game_code.Enemy import Enemy
from game_code.Player import Player

class EntityFactory:

    # NOTA: Factories não possuem construtor (método __init__ [dunder init])

    @staticmethod
    def build_entity(entity_name: str, position: tuple = (0, 0)):
        
        match entity_name:

            case 'Level1Bg':
                list_bg = []
                # 'range(7)' - remete a quantidade de imagens para formar o background1
                for i in range(0, 7, 1):

                    curr_level_name = f"Level1Bg{i}"
                    # Formando as imagens no começo da tela (position(0, 0))
                    list_bg.append(Background(curr_level_name, 'backgrounds', position))
                    # Formando as imagens no fim da tela 
                    list_bg.append(Background(curr_level_name, 'backgrounds', (WIN_WIDTH, 0)))

                return list_bg
            
            case 'Level2Bg':
                list_bg = []
                # 'range(5)' - remete a quantidade de imagens para formar o background2
                for i in range(0, 5, 1):

                    curr_level_name = f"Level2Bg{i}"
                    # Formando as imagens no começo da tela (position(0, 0))
                    list_bg.append(Background(curr_level_name, 'backgrounds', position))
                    # Formando as imagens no fim da tela 
                    list_bg.append(Background(curr_level_name, 'backgrounds', (WIN_WIDTH, 0)))

                return list_bg
            
            case 'Player1':
                return Player('Player1', 'characters', (10, (WIN_HEIGHT / 2) - 30))
            
            case 'Player2':
                return Player('Player2', 'characters', (10, (WIN_HEIGHT / 2) + 30))
            
            # Fabricando os inimigos 1 e 2 após a largura máxima da tela, para que eles venham de fora para dentro, e considerando uma altura aleatória utilizando a função 'randint()' da biblioteca 'random'
            case 'Enemy1':
                return Enemy('Enemy1', 'characters', (WIN_WIDTH + 10, randint(10, WIN_HEIGHT - 25)))
            
            case 'Enemy2':
                return Enemy('Enemy2', 'characters', (WIN_WIDTH + 10, randint(10, WIN_HEIGHT - 25)))