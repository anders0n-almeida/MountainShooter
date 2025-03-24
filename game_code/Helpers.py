import pygame

from game_code.Entity import Entity

# MÉTODO PARA APRESENTAÇÃO DE TEXTOS (os textos são tratados como IMAGEM)
def generate_text(window: pygame.surface.Surface, text_size: int, text: str, text_color: tuple, text_pos: tuple, target: str):

    text_font: pygame.font.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()

    if (target == "menu" or target == "pause"):
        text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)

    elif (target == "level"):
        text_rect: pygame.Rect = text_surf.get_rect(left = text_pos[0], top = text_pos[1])

    window.blit(source=text_surf, dest=text_rect)

def generate_debug_text(window: pygame.surface.Surface, entity, text: str, text_size: int = 14, text_color: tuple = (255, 255, 255), position: str = "above"):
    """
    Exibe um texto de depuração acima ou abaixo de uma entidade específica.
    
    :param window: Surface do pygame onde o texto será renderizado.
    :param entity: Objeto da entidade sobre a qual o texto será exibido.
    :param text: Texto a ser exibido.
    :param text_size: Tamanho da fonte do texto.
    :param text_color: Cor do texto (RGB).
    :param position: Posição do texto em relação à entidade ('above' ou 'below').
    """

    text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf = text_font.render(text, True, text_color).convert_alpha()
    # Referência inicial de centro do retângulo do texto: centralizado horizontalmente na entidade (entity.rect.centerx) e no topo em relação ao eixo Y
    text_rect = text_surf.get_rect(center=(entity.rect.centerx, entity.rect.top))

    if position == "below":
        # O TOPO DO RETÂNGULO DO TEXT (text_rect.top) deve ficar um pouco ABAIXO da entidade (entity.rect.bottom + 5)
        text_rect.top = entity.rect.bottom + 5 
    else:
        # A PARTE INFERIOR/BASE DO RETÂNGULO DO TEXTO (text_rect.bottom) deve ficar um pouco ACIMA da entidade (entity.rect.bottom + 5)
        text_rect.bottom = entity.rect.top - 5

    window.blit(text_surf, text_rect)

def find_entity(needle: str, haystack: list[Entity]) -> Entity:
    """
    Função que busca e retorna uma entidade específicada por nome em uma lista de entidades enviada como parâmetro
    """
    
    found_entity = None

    for entity in haystack:

        if entity.name == needle:
            found_entity = entity

        # else
        continue

    return found_entity