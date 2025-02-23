import pygame

# Inicializando o pacote do 'pygame' com todos os recursos necessários ao seu funcionamento
pygame.init()

# Criando uma janela para o jogo (surface) de tamanho 1280 x 800
window = pygame.display.set_mode(size = (1280, 800))

while True:
    
    # Capturando todos os EVENTOS do projeto
    for event in pygame.event.get():

        # Tratando o evento de clicar no botão para fechar a janela do jogo
        if (event.type == pygame.QUIT):
            pygame.quit()   # Fecha a janela
            quit()          # Encerra o pygame