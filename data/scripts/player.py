import pygame, math

class jogador(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.p1 = (-16 + x),(-24 + y)
        self.p2 = (-16 + x),(24 + y)
        self.p3 = (16 + x),(24 + y)
        self.p4 = (16 + x),(-24 + y)
        self.vel = 100

    def mostra(self,janela,janela_x,janela_y,angulo,cor):
        pygame.draw.polygon(janela,cor,[(((18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - -18 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + -18 * math.cos(angulo)) + janela_y/2)),(((-18 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((-18 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - 24 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + 24 * math.cos(angulo)) + janela_y/2))],1)

    def mostra_db(self,janela,janela_x,janela_y,angulo,cor):
        pygame.draw.polygon(janela,(255,0,0),[(((0 * math.cos(angulo) - 24 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + 24 * math.cos(angulo)) + janela_y/2)),(((0 * math.cos(angulo) - -24 * math.sin(angulo)) + janela_x/2),((0 * math.sin(angulo) + -24 * math.cos(angulo)) + janela_y/2))],1)
        pygame.draw.polygon(janela,(0,0,255),[(((-18 * math.cos(angulo) - 0 * math.sin(angulo)) + janela_x/2),((-18 * math.sin(angulo) + 0 * math.cos(angulo)) + janela_y/2)),(((18 * math.cos(angulo) - -0 * math.sin(angulo)) + janela_x/2),((18 * math.sin(angulo) + -0 * math.cos(angulo)) + janela_y/2))],1)



