from game_code.Consts import *
from game_code.Entity import Entity
from game_code.Enemy import Enemy
from game_code.Player import Player
from game_code.PlayerShot import PlayerShot
from game_code.EnemyShot import EnemyShot
from game_code.Helpers import generate_text, find_entity

class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        """[MÉTODO PRIVADO] Verifica se uma entididade atingiu o limite da tela do jogo"""

        if isinstance(entity, Enemy):

            # quando o lado/borda DIREITO/RIGHT (extremidade direita) do retângulo que representa a entidade for MENOR do que zero (alcançar a borda esquerda da tela), a entidade receberá valor de vida negativo e, consequêntemente, será destruída devido a verificação constante do método 'verify_health' que roda no Level
            if entity.rect.right <= 0:
                entity.health = -1

        if isinstance(entity, (PlayerShot, EnemyShot)):
            if entity.rect.right <= 0 or entity.rect.left >= WIN_WIDTH:
                entity.health = -1

    @staticmethod
    def __verify_collision_entity(entity1: Entity, entity2: Entity):
        """
        [MÉTODO PRIVADO] Verifica se uma entididade atingiu outra passível de receber dano.
        As entidade podem ser JOGADORES, INIMIGOS, TIROS DE JOGADORES OU TIROS DE INIMIGO
        """

        # Flag
        is_valid_interaction = False

        # Colisão entre TIROS e NAVES
        if isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            is_valid_interaction = True

        if isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            is_valid_interaction = True

        if isinstance(entity1, Player) and isinstance(entity2, EnemyShot):
            is_valid_interaction = True

        if isinstance(entity1, EnemyShot) and isinstance(entity2, Player):
            is_valid_interaction = True

        if (is_valid_interaction):

            # Se a resposta para PELO MENOS uma das condições for 'False', não há colisão
            if ((entity1.rect.right >= entity2.rect.left) and
                (entity1.rect.left <= entity2.rect.right) and
                (entity1.rect.bottom >= entity2.rect.top) and
                (entity1.rect.top <= entity2.rect.bottom)):

                entity1.health -= entity2.damage
                entity2.health -= entity1.damage

                entity1.last_damage = entity2.name
                entity2.last_damage = entity1.name

                # Se a entidade atingida for Player ou Enemy, aplica o efeito de dano (piscar vermelho)
                for entity in [entity1, entity2]:
                    if isinstance(entity, (Player, Enemy)):
                        entity.surf = entity.surf.copy()  # Copia a imagem atual
                        entity.surf.fill((255, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)  # Aplica o tom avermelhado
                        entity.is_damaged = True
                        entity.damage_timer = pygame.time.get_ticks()

    @staticmethod
    def manage_score(player_reference: Player, score_reference: int, action: str = 'give'):
        """Gerenciador de pontuação dos jogadores"""

        if (action == 'give'):

            player_reference.score += score_reference

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """"Gerenciador de colisões em geral"""

        for i in range(0, len(entity_list), 1):

            # Verificando colisão com as bordas do level
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

            # Verificandoa  colisão entre duas entidades (elimimando redundâncias)
            # Possíveis redundâncias: 
            # - Comparar Player1 (entity1) com Player1 (entity2)
            # - Se 'i' e 'j' sempre começassem ambas em 0, em algum momento haveriam comparações que já ocorreram em laços anteriores:
            # Ex.: Player1 (entity1) com Enemy1(entity2) - laço 3
            # Ex.: Enemy1 (entity1) com Player1(entity2) - laço 6
            # Definir que o valor inicial de 'j' será sempre 'i + 1' elimina essas redundâncias
            for j in range(i + 1, len(entity_list), 1):

                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Processa as ocorrências com entidades de acordo com a vida delas"""

        for entity in entity_list:
            
            # Caso um inimigo passível de ser destruído seja destruído
            if ((entity.health is not None) and (entity.health <= 0)):

                # Aumentando o score do jogador que destruir um inimigo
                # 'entity.last_damage is not None' - condição que garante que quem destruiu o inimigo foi um jogador e não a chegada ao fim do cenário
                if isinstance(entity, Enemy) and entity.last_damage is not None:

                    player_ref = 'Player1' if entity.last_damage == 'Player1Shot' else 'Player2'
                    player_ref = find_entity(player_ref, entity_list)

                    score_ref = 100 if entity.name == 'Enemy1' else 200

                    EntityMediator.manage_score(player_ref, score_ref)

                entity_list.remove(entity)
                # print(f"Entidade {entity.name} destruída!")