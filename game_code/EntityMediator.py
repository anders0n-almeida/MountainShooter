from game_code.Consts import *
from game_code.Entity import Entity
from game_code.Enemy import Enemy
from game_code.PlayerShot import PlayerShot
from game_code.EnemyShot import EnemyShot
from game_code.Helpers import generate_text

class EntityMediator:

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """"Gerenciador de colisões em geral"""

        for index, entity in enumerate(entity_list):

            EntityMediator.__verify_collision_window(entity)

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
    def verify_health(entity_list: list[Entity]):
        """Processa as ocorrências com entidades de acordo com a vida delas"""

        for entity in entity_list:
            
            if ((entity.health is not None) and (entity.health <= 0)):

                entity_list.remove(entity)
                # print(f"Entidade {entity.name} destruída!")