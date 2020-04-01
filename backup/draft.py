import pygame, sys, os
import numpy as np
from pygame.locals import *

pygame.init()
pygame.font.init()

fonte = pygame.font.Font('Hyper.otf',40)

# janela config

janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
janela_x, janela_y = pygame.display.get_surface().get_size()
pygame.display.set_caption("Jojinho")

# jogador config

j_x = janela_x / 2
j_y = janela_y / 2
j_v = 1
j_g = 10

o1_x = janela_x / 2
o1_y = janela_y * 2

f_fade = True

#funcs

def efeito_fade(tela_x,tela_y):
  
  fade = pygame.Surface((tela_x,tela_y))
  fade.fill((0,0,0))
  for alfa in range (0,300):
    fade.set_alpha(300-alfa)
    refazer_janela()
    janela.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(1)

def refazer_janela():
  
  janela.fill((255,255,255))
  pygame.draw.polygon(janela,(0,0,0),[(18+j_x,-24+j_y),(0+j_x,-18+j_y),(-18+j_x,-24+j_y),(0+j_x,24+j_y)],1)
  texty = fonte.render('Y : %r' %(f_fade), False, (0,0,0))
  textx = fonte.render('X : %d' %(j_y), False, (0,0,0))
  titulo = fonte.render('Starfall' , False, (0,0,0))
  janela.blit(titulo,(janela_x/2- janela_x/15,50))
  janela.blit(texty,(50,50))
  janela.blit(textx,(50,100))
  
#Game Loop

executar = True

while executar:
  pygame.time.delay(1)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      executar = False

  teclas = pygame.key.get_pressed()
  
  if teclas[pygame.K_LEFT]:
      if j_x >= 25:
        j_x -= j_v

  if teclas[pygame.K_RIGHT]:
    if j_x <= janela_x-25:     
        j_x += j_v

  if teclas[pygame.K_UP]:
    if j_y >= 40:
      j_y -= j_v

  if teclas[pygame.K_DOWN]:
    if j_y <= (janela_y/2)-50:
      j_y += j_v

  if teclas[pygame.K_ESCAPE]:
    executar = False

 #Render

  pygame.display.update()

  if f_fade:
    efeito_fade(janela_x,janela_y)
  f_fade = False

  refazer_janela()

pygame.quit()
