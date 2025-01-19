import pygame
import time

def load_mouth_images():
    mouth_images = {
        "rest": pygame.image.load("avatar(jpegs)\mouth_rest.jpg"),
        "a": pygame.image.load("avatar(jpegs)\mouth_a.jpg"),
        "e": pygame.image.load("avatar(jpegs)\mouth_e.jpg"),
        "i": pygame.image.load("avatar(jpegs)\mouth_i.jpg"),
        "o": pygame.image.load("avatar(jpegs)\mouth_o.jpg"),
        "u": pygame.image.load("avatar(jpegs)\mouth_u.jpg")
    }
    for key in mouth_images:
        mouth_images[key] = pygame.transform.scale(mouth_images[key], (200, 100))
    return mouth_images

def idle_animation(screen, mouth_rest, mouth_position):
    screen.blit(mouth_rest, mouth_position)
    pygame.display.flip()
    time.sleep(0.5)
