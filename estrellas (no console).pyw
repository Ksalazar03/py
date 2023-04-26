import pygame as pg
import numpy as np
from math import *
from time import *
import random


V = np.array
Height = 720
Width = 1280

ejey = Height/2
ejex = Width/2

def pos_screen(pos = V([])):
    
    return V([pos[0] + ejex, ejey - pos[1]])


def screen_pos(screen = V([])):

    return V([sreen[0] - ejex,  - screen[1]+ ejey])

class Ball():
    def __init__(self, pos,t,pase1,pase2):
        self.poso = pos
        self.pos = [pos,pos]
        self.t = 0
        l = t
        self.angle = 0
        self.huella= []
        self.run = True
        self.pase1 = pase1
        self.pase2 = pase2
        self.par = False
        self.tt = t
        n = 1
        def F(x):
            if x == -1:
                return pase1
            elif x == 1:
                return pase2
        self.punto = [pos]
        
        while n < 1000:
            
            
            self.punto.append( self.punto[-1] + V([cos(radians(self.angle)), sin(radians(self.angle))] )*l)
            self.angle += F((-1)**n)
            if (self.punto[0].round() == self.punto[-1].round()).all():                        
                break
            n+=1
            
        #print("n: ",n, " len: ", len(self.punto))
        self.n = n
        #print(self.punto)

            
            
            
    def update(self):
        
        if False:        
            self.pos [0]= self.pos[0] + V([cos(radians(self.angle)), sin(radians(self.angle))] )*4
            self.t+=1
            
            if self.t > self.tt:
                #self.tt *= 0.99
                #self.pos*=0
                self.t=0
                if self.par:
                    self.angle+=self.pase1
                    self.par=False
                else:
                    self.angle+=self.pase2
                    self.par = True
                for v in range(1,len(self.pos)):
                    
                        
                    if (self.pos[v].round() == self.pos[0].round()).all():                        
                        break
                    
                else:
                    self.pos.append(self.pos[0])

            if np.linalg.norm(self.pos[0]-self.poso) <= 1:
                self.run = False 
            
        
    def display(self):
        #print(len(self.pos))
        #pg.draw.circle(screen,"red",pos_screen(self.pos[0]),10)
        t = len(self.punto)
        for i in range(t):
            p1 = pos_screen(self.punto[i])
            if i == t-1:
                p2 = pos_screen(self.punto[0])
            else:
                p2 = pos_screen(self.punto[i+1])
            pg.draw.line(screen,"red",p1,p2,2)
                #pg.draw.circle(screen,"red",pos_screen(v),5)
        
        e = letra30.render("inflexiones: " + str(self.n), True,(200,200,200),(0,0,0))
        er = e.get_rect()
        er.centerx = 100
        er.centery = 400
        screen.blit(e,er)
        
            
        
class Manager():
    def __init__(self):
        self.q = 15
        self.e = 90
        self.t = 50
        self.reset()
        
    def reset(self):
        self.gameObjects = []
        pas = 5
        #for i in range(2,10):
         #   for j in range(2,10):
        self.gameObjects.append(Ball(V([0 ,0]),self.t,self.q,self.e))
        
        
    def update(self):
        for g in self.gameObjects:
            g.update()
    def onkeyup(self,key):
        print(key)
    def onkeydown(self,key):
        if key == 113:
            self.q+=1
            self.reset()
        if key == 101:
            self.e+=1
            self.reset()
        if key == 1073741903:
            self.q += 5
            self.reset()
        if key == 1073741904:
            self.q -= 5
            self.reset()
        if key == 1073741905:
            self.e -= 5
            self.reset()
        if key == 1073741906:
            self.e += 5
            self.reset()
        if key == 105:
            self.t +=5
            self.reset()
        if key == 107:
            self.t -=5
            self.reset()
        if key == 114:
            self.reset()
            
        
    def display(self):
        screen.fill("white")
        q = letra30.render("angulo 1: "+str(self.q), True,(200,200,200),(0,0,0))
        qr = q.get_rect()
        qr.centerx = 100
        qr.centery = 100
        screen.blit(q,qr)

        e = letra30.render("angulo 2: "+str(self.e), True,(200,200,200),(0,0,0))
        er = e.get_rect()
        er.centerx = 100
        er.centery = 200
        screen.blit(e,er)

        t = letra30.render("tamaño: "+str(self.t), True,(200,200,200),(0,0,0))
        tr = t.get_rect()
        tr.centerx = 100
        tr.centery = 300
        screen.blit(t,tr)
        
        for g in self.gameObjects:
            g.display()
        
        
        
pg.init()

screen = pg.display.set_mode((1280,720))
letra30 = pg.font.SysFont("Arial",30)

clock = pg.time.Clock()
running = True

manager = Manager()

        
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            manager.onkeydown(event.key)
        elif event.type == pg.KEYUP:
            
            manager.onkeyup(event.key)            

    manager.update()
    manager.display()
    
    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()


