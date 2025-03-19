import pygame

# MÉTODO PARA APRESENTAÇÃO DE TEXTOS (os textos são tratados como IMAGEM)
def generate_text(window: pygame.surface.Surface, text_size: int, text: str, text_color: tuple, text_pos: tuple, target: str):

    text_font: pygame.font.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()

    if (target == "menu" or target == "pause"):
        text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)

    elif (target == "level"):
        text_rect: pygame.Rect = text_surf.get_rect(left = text_pos[0], top = text_pos[1])

    window.blit(source=text_surf, dest=text_rect)