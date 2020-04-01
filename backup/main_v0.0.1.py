import pygame, sys, os, math, random, string
import numpy as np
from pygame.locals import *

'''
Variáveis / Inicializadores, Etc..
'''

pygame.init()
pygame.font.init()

fonte = pygame.font.Font('Hyper.otf',40)
tit = pygame.font.Font('Hyper.otf',250)

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

intro = True
debbug = False

#cores
preto = (0,0,0)
preto_f = (0,0,0)
branco = (255,255,255)
branco_f = (255,255,255)

'''
Funções
'''

def glitch_string(tamanho):
  texto_glitch = string.ascii_letters + string.digits
  return ''.join(random.choice(texto_glitch) for i in range(tamanho))

def objeto_quadrado(posição_x,posição_y,cor_f):
  
  pygame.draw.polygon(janela,cor_f,[(50+posição_x+x_ds,50+posição_y+y_ds),(-50+posição_x+x_ds,50+posição_y+y_ds),(-50+posição_x+x_ds,-50+posição_y+y_ds),(50+posição_x+x_ds,-50+posição_y+y_ds)])

def efeito_fade(tela_x,tela_y): # efeito de transição
  
  fade = pygame.Surface((tela_x,tela_y))
  fade.fill(branco)
  for alfa in range (0,300):
    fade.set_alpha(300-alfa)
    refazer_janela()
    janela.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(1)


def fade_titulo(tela_x,tela_y): # Controla a intro

  fade = pygame.Surface((tela_x,tela_y))
  fade.fill(branco)
  for alfa in range (0,300):
    fade.set_alpha(300-alfa)
    texto_tit = tit.render('STARFALL', False, preto)
    janela.blit(texto_tit,(tela_x/8,tela_y/3.5))
    janela.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(1)
  pygame.time.delay(3000)
  for beta in range (0,300):
    fade.set_alpha(beta)
    texto_tit = tit.render('STARFALL', False, preto)
    janela.blit(texto_tit,(tela_x/8,tela_y/3.5))
    janela.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(1)
  fade.set_alpha(0)

def refazer_janela(): # Refresh de imagem
  
  janela.fill(branco)

  #objeto
  objeto_quadrado(350,750,preto_f)
  objeto_quadrado(450,750,branco_f)

  #textos
  nada_e = fonte.render('Bem vindo!', True, preto_f)
  parece = fonte.render('%s' %(glitch_string(8)), True, branco_f)

  janela.blit(nada_e,(300+x_ds,200+y_ds))
  janela.blit(parece,(300+x_ds,250+y_ds))

  #jogador
  pygame.draw.polygon(janela,preto,[(((18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - -18 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + -18 * math.cos(angulo)) + janela_y/2)),(((-18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((-18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - 24 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + 24 * math.cos(angulo)) + janela_y/2))],1)

  if debbug == True:
    titulo = fonte.render('Starfall v:0.0.1' , False, preto)
    texty = fonte.render('X : %d' %(j_x), False, preto)
    textx = fonte.render('Y : %d' %(j_y), False, preto)
    textz = fonte.render('Ang : %d' %(angulo), False, preto)
    textsen = fonte.render('Sen : %d' %(se), False, preto)
    textco = fonte.render('Cos : %d' %(co), False, preto)
    textbug = fonte.render('Debug mode: ON', False, (255,0,0))
    textx_ds = fonte.render('X_ds: %d' %x_ds, False, preto)
    texty_ds = fonte.render('Y_ds: %d' %y_ds, True, preto)

    janela.blit(titulo,(50,50))
    janela.blit(texty,(50,100))
    janela.blit(textx,(50,150))
    janela.blit(textz,(50,200))
    janela.blit(textsen,(50,250))
    janela.blit(textco,(50,300))
    janela.blit(textbug,(50,350))
    janela.blit(textx_ds,(50,400))
    janela.blit(texty_ds,(50,450))

'''
Gameloop
'''

executar = True

while executar:
  pygame.time.delay(1)

  co = (math.cos(angulo)*180/math.pi)
  se = (math.sin(angulo)*180/math.pi)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      executar = False

  teclas = pygame.key.get_pressed()
  
  if teclas[pygame.K_a]:
    angulo -= 0.01

  if teclas[pygame.K_d]:
    angulo += 0.01

  if teclas[pygame.K_w]:
      j_x += math.sin(angulo) * j_v
      j_y += -math.cos(angulo) * j_v
      
  if teclas[pygame.K_s]:
      j_x -= math.sin(angulo) * j_v
      j_y -= -math.cos(angulo) * j_v

  if teclas[pygame.K_ESCAPE]:
    executar = False

  if teclas[pygame.K_F3]:  
      if debbug == False:
        debbug = True

  if teclas[pygame.K_F2]:
    if debbug == True:
      debbug = False

  if teclas[pygame.K_q]:
    preto = (255,255,255)
    branco = (0,0,0)

  if teclas[pygame.K_e]:
    preto = (0,0,0)
    branco = (255,255,255)

  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LSHIFT:
      j_v = 2
    else:
      j_v = 1

  x_ds = j_x - janela_x/2
  y_ds = j_y - janela_y/2

 #Render

  pygame.display.update()

  if intro:
    fade_titulo(janela_x,janela_y)
    intro = False
    efeito_fade(janela_x,janela_y)

  refazer_janela()

pygame.quit()
