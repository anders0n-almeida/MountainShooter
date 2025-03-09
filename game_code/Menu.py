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
            curr_y_pos = 180
            for option in MENU_OPTIONS:

                self.menu_text(15, option, COLOR_WHITE, ((WIN_WIDTH / 2), curr_y_pos))
                curr_y_pos += 30

            # atualizando a tela para apresentar a imagem
            pygame.display.flip()

            # Capturando todos os EVENTOS do projeto
            for event in pygame.event.get():

                # Tratando o evento de clicar no botão para fechar a janela do jogo
                if (event.type == pygame.QUIT):
                    pygame.quit()   # Fecha a janela
                    quit()          # Encerra o pygame

    # MÉTODO PARA APRESENTAÇÃO DE TEXTOS NO MENU (os textos são tratados como IMAGEM)
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        text_font: pygame.font.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)