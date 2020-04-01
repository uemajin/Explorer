import pygame, sys, os, math, random, string
import numpy as np
from data.scripts.player import *

'''
Variáveis / Inicializadores, Etc..
'''
pygame.init()
pygame.font.init()

fonte = pygame.font.Font(os.path.abspath('data/text/Hyper.otf'),40)
tit = pygame.font.Font(os.path.abspath('data/text/Hyper.otf'),250)

#cores
preto = (0,0,0)
preto_f = (0,0,0)
branco = (255,255,255)
branco_f = (255,255,255)

angulo = 0
2
# janela config

janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
janela_x, janela_y = pygame.display.get_surface().get_size()
pygame.display.set_caption("Jojinho")

# jogador config

jog_1 = jogador(janela_x/2,janela_y/2)

intro = True
debbug = False


'''
Funções
'''

def debbug_print():

  co = (math.cos(angulo)*180/math.pi)
  se = (math.sin(angulo)*180/math.pi)
  
  jog_1.mostra_db(janela,janela_x,janela_y,angulo,preto)
  titulo = fonte.render('エクスプローラー v:0.0.1' , False, preto)
  texty = fonte.render('X : %d' %(jog_1.x), False, preto)
  textx = fonte.render('Y : %d' %(jog_1.y), False, preto)
  textz = fonte.render('Ang : %d' %(angulo), False, preto)
  textsen = fonte.render('Sen : %d' %(se), False, preto)
  textco = fonte.render('Cos : %d' %(co), False, preto)
  textbug = fonte.render('デブゴ: ON', False, (255,0,0))
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

def glitch_string(tamanho):
  texto_glitch = string.ascii_letters + string.digits
  return ''.join(random.choice(texto_glitch) for i in range(tamanho))

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

  #textos
  nada_e = fonte.render('Bem vindo!', True, preto_f)
  parece = fonte.render('%s' %(glitch_string(8)), True, branco_f)

  janela.blit(nada_e,(300+x_ds,200+y_ds))
  janela.blit(parece,(300+x_ds,250+y_ds))

  #jogador
  jog_1.mostra(janela,janela_x,janela_y,angulo,preto)
      
  if debbug == True:
    debbug_print()
    
'''
Gameloop
'''

executar = True

while executar:
  pygame.time.delay(1)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      executar = False

  teclas = pygame.key.get_pressed()
  
  if teclas[pygame.K_a]:
    angulo -= 0.1

  if teclas[pygame.K_d]:
    angulo += 0.1

  if teclas[pygame.K_w]:
      jog_1.x += math.sin(angulo) * jog_1.vel*2
      jog_1.y += -math.cos(angulo) * jog_1.vel*2
      
  if teclas[pygame.K_s]:
      jog_1.x -= math.sin(angulo) * jog_1.vel*2
      jog_1.y -= -math.cos(angulo) * jog_1.vel*2

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
      jog_1.vel = 2
    else:
      jog_1.vel = 1

  x_ds = jog_1.x - janela_x/2
  y_ds = jog_1.y - janela_y/2

 #Render  
  pygame.display.update()

  if intro:
    #fade_titulo(janela_x,janela_y) # Intro
    #efeito_fade(janela_x,janela_y) # Fade 
    intro = False

  refazer_janela()

pygame.quit()
