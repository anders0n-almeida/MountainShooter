# Importações gerais
import pygame

# Importações do Python Package 'game_code'
from game_code.Consts import WIN_WIDTH, WIN_HEIGHT 
from game_code.Menu import Menu
from game_code.Level import Level
from game_code.Score import Score



class Game:

    def __init__(self):
         # Inicializando o pacote do 'pygame' com todos os recursos necessários ao seu funcionamento
        pygame.init()

        # Criando uma janela para o jogo (surface) de tamanho 576 x 324 (tamanho das imagens de cenários baixadas) através da inicialização do atributo 'window' dos objetos instaciados pela classe Game
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    # O JOGO INICIA DAQUI
    def run(self):

        while True:

            # Chamando a tela de MENU e instanciando a tela de SCORE
            menu = Menu(self.window)
            score = Score(self.window)

            # A variável 'menu_response' recebe o retorno do menu (opção escolhida)
            menu_response = menu.run()

            # tratando a opção recebida pelo menu
            match (menu_response):

                case 'NEW GAME [1P]' | 'NEW GAME [2P] - COOPERATIVE' | 'NEW GAME [2P] - COMPETITIVE':
                    
                    # lista de pontuação (posição 01/index 0 - Player1 / posição 02/index 1 - Player2)
                    player_score = [0, 0]

                    level = Level(self.window, 'Level1', menu_response, player_score)
                    level_response = level.run(player_score)

                    if level_response == "menu":
                        continue  # Volta ao menu

                    elif level_response == "level_complete":

                        level = Level(self.window, 'Level2', menu_response, player_score)
                        level_response = level.run(player_score)

                        if level_response == "level_complete":

                            # devo passar como parâmetro a resposta do menu/opção do menu selecionada para saber se trata-se de um jogo de 1 ou 2 jogadores
                            score.save(menu_response, player_score)

                case 'SCORE':

                    score_response = score.show()

                    if score_response == "menu":
                        continue  # Volta ao menu

                case 'EXIT':
                    pygame.quit()
                    quit()