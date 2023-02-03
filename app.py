import pygame
import os
import random

Tela_largura = 500
Tela_Altura = 800

Imagens_Passaro = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png'))),
]

Imagen_Cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
Imagens_Chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
Imagens_Backgroud = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

pygame.font.init()
Fonte_Pontos = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = Imagens_Passaro
    #Animações da rotação
    Rotacao_Maxima = 25
    Velociadade_Rotacao = 20
    Tempo_Animacao = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velociadade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagen = 0
        self.imagem = IMGS[0]

class Cano:
    pass

class Chao:
    pass