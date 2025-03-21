import pygame

# DEFINIÇÃO DE CONSTANTES PARA O JOGO

# TAMANHOS / POSIÇÕES
WIN_WIDTH = 576
WIN_HEIGHT = 324

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_GREEN = (61, 238, 33)

# TECLAS
PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
    'Player2': pygame.K_KP_8
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
    'Player2': pygame.K_KP_2
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
    'Player2': pygame.K_KP_4
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_d,
    'Player2': pygame.K_KP_6
}

PLAYER_KEY_SHOT = {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_KP_ENTER
}

# ENTIDADES
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

ENTITY_HEALTH = {
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 40,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 175,
}

# EVENTOS
EVENT_ENEMY = pygame.USEREVENT + 1

# OUTROS
MENU_OPTIONS = [
    'NEW GAME [1P]',
    'NEW GAME [2P] - COOPERATIVE',
    'NEW GAME [2P] - COMPETITIVE',
    'SCORE',
    'EXIT'
]