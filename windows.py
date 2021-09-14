from pygame_init import pygame

info = pygame.display.Info()

WIDTH = info.current_w
HEIGHT = info.current_h
RESIZE_K = WIDTH / 1920


def calculate(value):
    return int(value * RESIZE_K)
