import pygame
import random

from game_code.Consts import *
from game_code.Entity import Entity
from game_code.EntityFactory import EntityFactory
from game_code.EntityMediator import EntityMediator
from game_code.Player import Player
from game_code.Enemy import Enemy
from game_code.Helpers import generate_debug_text, generate_text

class Level:

    def __init__(self, window: pygame.surface.Surface, level_name: str, game_mode):

        self.window = window
        self.level_name = level_name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 120000 # 120 segundos ou 2 minuntos
        self.paused = False  # Flag para indicar se o jogo está pausado

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
            pygame.mixer_music.set_volume(0.05)

            clock = pygame.time.Clock()

            while True:

                # FPS
                clock.tick(60)

                # Atualização das entidades caso o jogo NÃO ESTEJA PAUSADO
                if not self.paused:

                    # Atualizações constantes baseadas em ENTIDADES
                    for entity in self.entity_list:
                        self.window.blit(source=entity.surf, dest=entity.rect)
                        entity.move()

                        if isinstance(entity, (Player, Enemy)):
                            ent_shot = entity.shoot()
                            if ent_shot is not None:
                                self.entity_list.append(ent_shot)

                        # Caso a entidade pertinente receba dano, gerar o efeito de "piscar vermelho"
                        if isinstance(entity, (Player, Enemy)) and entity.is_damaged:
                            if pygame.time.get_ticks() - entity.damage_timer > 200:  # 200ms de piscar
                                entity.surf = entity.original_image  # Restaura a imagem original
                                entity.is_damaged = False

                        # Exibindo textos de vida e score dos jogadores
                        if entity.name == 'Player1':
                            generate_text(self.window, 14, f"Player 01 - Health: {entity.health} | Score {entity.score}", COLOR_GREEN, (10, 25), "level")
                        
                        if entity.name == 'Player2':
                            generate_text(self.window, 14, f"Player 02 - Health: {entity.health} | Score {entity.score}", COLOR_CYAN, (10, 45), "level")

                        # # Gerando um texto abaixo do inimigo
                        # if isinstance(entity, (Player, Enemy)):x'
                        #     generate_debug_text(self.window, entity, f"{entity.health}", position="below")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.toggle_pause()
                    
                    # Gerando inimigos aleatoriamente dentro de um tempo específico
                    if (event.type == EVENT_ENEMY) and (not self.paused):
                        enemy_choice = random.choice(('Enemy1', 'Enemy2'))
                        self.entity_list.append(EntityFactory.build_entity(enemy_choice))
                
                # Textos do LEVEL no canto SUPERIOR ESQUERDO
                generate_text(self.window, 14, f"{self.level_name} - Tempo: {(self.timeout / 1000):.2f}", COLOR_WHITE, (10, 5), "level")

                # Textos do LEVEL no canto INFERIOR ESQUERDO
                generate_text(self.window, 14, f"FPS: {clock.get_fps():.0f}", COLOR_WHITE, (10, WIN_HEIGHT - 35), "level")
                generate_text(self.window, 14, f"ENTIDADES: {len(self.entity_list)}", COLOR_WHITE, (10, WIN_HEIGHT - 20), "level")

                if self.paused:
                    response = self.draw_pause_screen()
                    if response == "menu":
                        return "menu"  # Sai completamente do loop do jogo e volta ao menu

                pygame.display.flip()

                # Tratamento de COLISÕES
                EntityMediator.verify_collision(self.entity_list)
                EntityMediator.verify_health(self.entity_list)

    def toggle_pause(self):
        """Ativa ou desativa a pausa do jogo"""
        self.paused = not self.paused

        if self.paused:
            pygame.mixer_music.pause()
        else:
            pygame.mixer_music.unpause()

    def draw_pause_screen(self):
        """Desenha a tela de pausa"""
        overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        overlay.set_alpha(150)  # Transparência
        overlay.fill((0, 0, 0))
        self.window.blit(overlay, (0, 0))

        generate_text(self.window, 30, "JOGO PAUSADO", COLOR_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT / 3), "pause")
        generate_text(self.window, 20, "Pressione ESC para continuar ou ENTER para sair", COLOR_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT / 2), "pause")

        pygame.display.flip()

        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.toggle_pause()
                    elif event.key == pygame.K_RETURN:
                        return "menu"