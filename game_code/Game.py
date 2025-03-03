# Importações do Python Package 'game_code'
from game_code.Consts import WIN_WIDTH, WIN_HEIGHT 
from game_code.Menu import Menu

# Importações gerais
import pygame

class Game:

    def __init__(self):
         # Inicializando o pacote do 'pygame' com todos os recursos necessários ao seu funcionamento
        pygame.init()

        # Criando uma janela para o jogo (surface) de tamanho 576 x 324 (tamanho das imagens de cenários baixadas) através da inicialização do atributo 'window' dos objetos instaciados pela classe Game
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            # Chamando a tela de MENU
            menu = Menu(self.window)
            menu.run()