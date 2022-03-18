print(' ==== Desafio 21 ====')

import pygame

#Iniciando o Pygame Mixer
pygame.mixer.init()

#Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('Ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()