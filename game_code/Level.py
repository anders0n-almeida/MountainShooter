import pygame
import random

from game_code.Consts import *
from game_code.Entity import Entity
from game_code.EntityFactory import EntityFactory
from game_code.Helpers import generate_text

class Level:

    def __init__(self, window: pygame.surface.Surface, level_name: str, game_mode):

        self.window = window
        self.level_name = level_name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 120000 # 120 segundos ou 2 minuntos

        self.entity_list.extend(EntityFactory.build_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.build_entity('Player1'))

        if (game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]):
            self.entity_list.append(EntityFactory.build_entity('Player2'))

        # a cada intervalo de tempo específico (no caso atual, 4 segundos), instancia um inimigo
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):

        while True:

            pygame.mixer_music.load(f"assets/sounds/soundtrack/{self.level_name}.mp3")
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.15)

            clock = pygame.time.Clock()

            while True:

                # FPS
                clock.tick(60)

                for entity in self.entity_list:
                    self.window.blit(source = entity.surf, dest = entity.rect)
                    entity.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == EVENT_ENEMY:
                        enemy_choice = random.choice(('Enemy1', 'Enemy2'))
                        self.entity_list.append(EntityFactory.build_entity(enemy_choice))

                generate_text(self.window, 14, f"{self.level_name} - Tempo: {(self.timeout / 1000):.2f}", COLOR_WHITE, (10, 5), "level")
                generate_text(self.window, 14, f"FPS: {clock.get_fps():.0f}", COLOR_WHITE, (10, WIN_HEIGHT - 35), "level")
                generate_text(self.window, 14, f"ENTIDADES: {len(self.entity_list)}", COLOR_WHITE, (10, WIN_HEIGHT - 20), "level")

                pygame.display.flip()