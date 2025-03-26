import pygame

from game_code.DBProxy import DBProxy
from game_code.Helpers import generate_text, get_curr_formatted_date
from game_code.Consts import *

class Score:

    def __init__(self, window: pygame.surface.Surface):

        self.window = window

        # carregando a imagem do score
        self.surf = pygame.image.load('./assets/backgrounds/ScoreBg.png').convert_alpha()

        # criando um retângulo invisível (posteriormente, a imagem carregada será inserida dentro desse retângulo)
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def save(self, game_mode: str, player_score: list[int]):

        pygame.mixer_music.load('./assets/sounds/soundtrack/Score.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.25)

        db_proxy = DBProxy('db_score')
        winner_name = ""
        
        while True:
            
            self.window.blit(source = self.surf, dest = self.rect)

            generate_text(self.window, 48, "WIN", COLOR_GREEN, SCORE_POS['title'], "score")

            if game_mode == 'NEW GAME [1P]':

                score = player_score[0]
                text = 'Congratulations, Player1! Enter your name [4 characters]: '

            elif game_mode == 'NEW GAME [2P] - COOPERATIVE':

                score = player_score[0] + player_score[1]
                text = 'Congratulations, Team! Enter your name [4 characters]: '

            elif game_mode == 'NEW GAME [2P] - COMPETITIVE':

                score = max(player_score)
                winner = 'Player1' if player_score[0] > player_score[1] else 'Player2'

                text = f'Congratulations, {winner}! Enter your name [4 characters]: '

            generate_text(self.window, 15, text, COLOR_WHITE, SCORE_POS['enter_name'], "score")

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

                if (event.type == pygame.KEYDOWN):

                    if (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) and len(winner_name) == 4:

                        db_proxy.save({'name': winner_name, 'score': score, 'date': get_curr_formatted_date()})
                        self.show()
                        return "menu"

                    elif (event.key == pygame.K_BACKSPACE):

                        winner_name = winner_name[:-1]

                    else:

                        if len(winner_name) < 4:

                            winner_name += event.unicode

            generate_text(self.window, 20, winner_name, COLOR_WHITE, SCORE_POS['name'], "score")

            pygame.display.flip()


    def show(self):

        # Carregar a música para o score
        pygame.mixer_music.load('./assets/sounds/soundtrack/Score.mp3')
        
        # Tocando a música carregada indefinidamente (argumento -1) e ajustando o volume
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.25)

        db_proxy = DBProxy('db_score')
        score_list = db_proxy.retrieve_top10()
        db_proxy.close()

        # desenhando a imagem carregada (self.surf) no retângulo invisível 'self.rect'
        self.window.blit(source = self.surf, dest = self.rect)

        generate_text(self.window, 48, 'TOP 10 SCORE', COLOR_CYAN, SCORE_POS['title'], "score")
        generate_text(self.window, 20, 'NAME    SCORE       DATE   ', COLOR_CYAN, SCORE_POS['label'], "score")

        for player_score in score_list:

            # desempacotando a lista em variáveis (método pythonico)
            id_, name, score, date = player_score

            generate_text(self.window, 20, f'{name}  {score:05d}  {date}', COLOR_CYAN, SCORE_POS[score_list.index(player_score)], "score")

        while True:

            # atualizando a tela para apresentar a imagem
            pygame.display.flip()

            # Capturando todos os EVENTOS do projeto
            for event in pygame.event.get():

                # Tratando o evento de clicar no botão para fechar a janela do jogo
                if (event.type == pygame.QUIT):
                    pygame.quit()   # Fecha a janela
                    quit()          # Encerra o pygame

                if (event.type == pygame.KEYDOWN):

                    if event.key == pygame.K_ESCAPE:

                        return "menu"