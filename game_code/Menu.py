# Importações gerais
import pygame

# Importações do Python Package 'game_code' (MÓDULOS INTERNOS)
from game_code.Consts import *

class Menu:

    # CONSTRUTOR
    # A janela enviada como argumento para o parâmetro 'window' precisa ser do tipo 'Surface', importado do pygame
    def __init__(self, window: pygame.surface.Surface):
        self.window = window

        # carregando a imagem do menu
        self.surface_img_place = pygame.image.load('./assets/backgrounds/MenuBg.png')

        # criando um retângulo invisível (posteriormente, a imagem carregada será inserida dentro desse retângulo)
        self.rect = self.surface_img_place.get_rect(left = 0, top = 0)

    # MÉTODO RODAR/RUN
    def run(self):

        # Opção inicial de seleção do menu
        curr_menu_option = 0
        
        # Carregar a música para o menu
        pygame.mixer_music.load('./assets/sounds/soundtrack/Menu.mp3')
        
        # Tocando a música carregada indefinidamente (argumento -1)
        pygame.mixer_music.play(-1)

        while True:
            
            # desenhando a imagem carregada (self.surface_img_place) no retângulo invisível 'self.rect'
            self.window.blit(source = self.surface_img_place, dest = self.rect)

            # desenhando os textos do menu (são tratados como imagem) [CORES DEFINIDAS NO ARQUIVO 'Conts.py']
            # [NOTA]: A ordem IMPORTA! Se você desenhar a imagem depois de escrever o texto, a imagem irá sobrepor o texto
            # TÍTULO
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # MENU
            for i in range(0, len(MENU_OPTIONS), 1):
                if i == curr_menu_option:
                    self.menu_text(15, MENU_OPTIONS[i], COLOR_GREEN, ((WIN_WIDTH / 2), 180 + (30) * i))
                else:
                    self.menu_text(15, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + (30) * i))

            # atualizando a tela para apresentar a imagem
            pygame.display.flip()

            # Capturando todos os EVENTOS do projeto
            for event in pygame.event.get():

                # Tratando o evento de clicar no botão para fechar a janela do jogo
                if (event.type == pygame.QUIT):
                    pygame.quit()   # Fecha a janela
                    quit()          # Encerra o pygame

                # Tratando o evento de pressionar teclas no MENU
                if (event.type == pygame.KEYDOWN):
                    # Seta para baixo
                    if event.key == pygame.K_DOWN:

                        if (curr_menu_option < (len(MENU_OPTIONS) - 1)):
                            curr_menu_option += 1

                    # Seta para cima
                    elif event.key == pygame.K_UP:

                        if (curr_menu_option > 0):
                            curr_menu_option -= 1

                    # Tecla ENTER ou BARRA DE ESPAÇO
                    elif (event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE):

                        return MENU_OPTIONS[curr_menu_option]; 

    # MÉTODO PARA APRESENTAÇÃO DE TEXTOS NO MENU (os textos são tratados como IMAGEM)
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        text_font: pygame.font.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)