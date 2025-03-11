# Importações do Python Package 'game_code'
from game_code.Consts import WIN_WIDTH, WIN_HEIGHT 
from game_code.Menu import Menu
from game_code.Level import Level

# Importações gerais
import pygame

class Game:

    def __init__(self):
         # Inicializando o pacote do 'pygame' com todos os recursos necessários ao seu funcionamento
        pygame.init()

        # Criando uma janela para o jogo (surface) de tamanho 576 x 324 (tamanho das imagens de cenários baixadas) através da inicialização do atributo 'window' dos objetos instaciados pela classe Game
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    # O JOGO INICIA DAQUI
    def run(self):

        while True:

            # Chamando a tela de MENU
            menu = Menu(self.window)
            # A variável 'menu_response' recebe o retorno do menu (opção escolhida)
            menu_response = menu.run()

            # tratando a opção recebida pelo menu
            match (menu_response):

                case 'NEW GAME [1P]' | 'NEW GAME [2P] - COOPERATIVE' | 'NEW GAME [2P] - COMPETITIVE':
                    
                    level = Level(self.window, 'Level 01', menu_response)
                    level_response = level.run()

                case 'SCORE':
                    ...

                case 'EXIT':
                    pygame.quit()
                    quit()