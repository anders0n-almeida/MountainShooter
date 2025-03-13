from game_code.Background import Background
from game_code.Consts import *

class EntityFactory:

    # NOTA: Factories não possuem construtor (método __init__ [dunder init])

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        
        match entity_name:

            case 'Level1Bg':
                list_bg = []
                for i in range(0, 7, 1):

                    curr_level_name = f"Level1Bg{i}"
                    # Formando as imagens no começo da tela (position(0, 0))
                    list_bg.append(Background(curr_level_name, 'backgrounds', position))
                    # Formando as imagens no fim da tela 
                    list_bg.append(Background(curr_level_name, 'backgrounds', (WIN_WIDTH, 0)))

                return list_bg