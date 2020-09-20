import pygame
import time
import random
from random import randint
import math


pygame.init()

WIDTH, HEIGHT = 500, 500
TILEWIDTH, TILEHEIGHT = 50, 50
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
class Tile:
    def __init__(self,x,y,r,g,b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.links = [1,1,1,1]

    def draw(self):
        xcoor = self.x * (WIDTH/TILEWIDTH)
        ycoor = self.y * (HEIGHT/TILEHEIGHT)
        pygame.draw.rect(WIN,(self.r,self.g,self.b),(xcoor,ycoor, WIDTH/TILEWIDTH, HEIGHT/TILEHEIGHT))
        if self.links[0] == 1:
            pygame.draw.line(WIN,(255,255,255),(xcoor,ycoor),(xcoor + (WIDTH/TILEWIDTH),ycoor), 2)
        if self.links[1] == 1:
            pygame.draw.line(WIN, (255, 255, 255), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor + (WIDTH/TILEWIDTH), ycoor), 2)
        if self.links[2] == 1:
            pygame.draw.line(WIN, (255, 255, 255), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        if self.links[3] == 1:
            pygame.draw.line(WIN, (255, 255, 255), (xcoor, ycoor), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        return

class Maze:
    tiles = []
    def __init__(self,w,h):
        for i in range(w):
            temp = []
            for j in range(h):
                temp.append(Tile(j,i,randint(0,255),randint(0,255),randint(0,255)))
            self.tiles.append(temp)

    def draw(self):
        for i in self.tiles:
            for j in i:
                j.draw()

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    print('HERE')
    M = Maze(TILEWIDTH,TILEHEIGHT)
    M.draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main()