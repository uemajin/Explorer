import pygame, sys, os, math, random
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

angulo = 0

o1_x = janela_x / 2
o1_y = janela_y * 2

f_fade = True
mudar = False

#funcs

#def desenhar_objeto(tela,pontos[]):
  #pygame.draw.polygon(tela,(0,0,0),pontos,1)

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

  #jogador
  pygame.draw.polygon(janela,(0,0,0),[(((18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - -18 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + -18 * math.cos(angulo)) + janela_y/2)),(((-18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((-18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - 24 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + 24 * math.cos(angulo)) + janela_y/2))],1)

  #objeto
  pygame.draw.polygon(janela,(0,0,255),[(380+j_x,421+j_y),(390+j_x,400+j_y),(403+j_x,480+j_y),(400+j_x,440+j_y)])

  texty = fonte.render('X : %d' %(j_x), False, (0,0,0))
  textx = fonte.render('Y : %d' %(j_y), False, (0,0,0))
  textz = fonte.render('Ang : %d' %(angulo), False, (0,0,0))
  textsen = fonte.render('Sen : %d' %(se), False, (0,0,0))
  textco = fonte.render('Cos : %d' %(co), False, (0,0,0))  

  titulo = fonte.render('Starfall' , False, (0,0,0))
  
  janela.blit(titulo,(janela_x/2- janela_x/15,50))
  
  janela.blit(texty,(50,50))
  janela.blit(textx,(50,100))
  janela.blit(textz,(50,150))
  janela.blit(textsen,(50,200))
  janela.blit(textco,(50,250))

#Game Loop

executar = True

while executar:
  pygame.time.delay(1)

  co = (math.cos(angulo)*180/math.pi)
  se = (math.sin(angulo)*180/math.pi)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      executar = False

  teclas = pygame.key.get_pressed()
  
  if teclas[pygame.K_LEFT]:
    angulo -= 0.01

  if teclas[pygame.K_RIGHT]:
    angulo += 0.01

  if teclas[pygame.K_UP]:
      j_x += math.sin(angulo) * j_v
      j_y += -math.cos(angulo) * j_v
      
  if teclas[pygame.K_DOWN]:
      j_y -= j_v

  if teclas[pygame.K_ESCAPE]:
    executar = False




 #Render

  pygame.display.update()

  if f_fade:
    efeito_fade(janela_x,janela_y)
  f_fade = False

  refazer_janela()

pygame.quit()
