import os
from pygame_init import pygame


def load_image(name, size):
    image = pygame.transform.scale(pygame.image.load(os.path.join(images_folder, name)), size)
    if name[-3] == "j":
        return image.convert()
    return image.convert_alpha()


images_folder = "assets/images"
