import pygame
import time
import random
from random import randint
import math


pygame.init()

WIDTH, HEIGHT = 500, 500
TILEWIDTH, TILEHEIGHT = 10, 10
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
        print('drawing ' + str(xcoor) + ' ' + str(ycoor) + ' ' + str(self.r) + str(self.g) + str(self.b))
        pygame.draw.rect(WIN,(self.r,self.g,self.b),(xcoor,ycoor, WIDTH/TILEWIDTH, HEIGHT/TILEHEIGHT))
        if self.links[0] == 1:
            pygame.draw.line(WIN,(0,0,0),(xcoor,ycoor),(xcoor + (WIDTH/TILEWIDTH),ycoor), 2)
        if self.links[1] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor + (WIDTH/TILEWIDTH), ycoor), 2)
        if self.links[2] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        if self.links[3] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor, ycoor), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        return

    def setLink(self,n):
        self.links[n] = 0

    def setRGB(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

class Maze:
    tiles = []
    links = []
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

    def set(self,x,y,r,g,b):
        print('setting ' + str(x) + ' ' + str(y))
        self.tiles[y][x].setRGB(r,g,b)
        self.tiles[y][x].draw()

    def getTile(self,x,y):
        if x < 0 or y < 0 or x >= TILEWIDTH or y >= TILEHEIGHT:
            return 0
        return self.tiles[x][y]

class MazeMaker:
    h = {}
    def mazify(self, m):
        self.visit(0,0,m)

    def visit(self,x,y,m):
        print('VISITING ' + str(x) + ' ' + str(y))
        if m.getTile(x,y) == 0:
            print('invalid')
            return
        m.set(x,y,255,255,255)
        self.h[m.getTile(x,y)] = randint(0,1000)
        j = list(range(4))
        random.shuffle(j)
        for i in j:
            if j[i] == 0 and (m.getTile(x,y-1) not in self.h.keys()) and m.getTile(x,y-1) != 0:
                m.getTile(x,y).setLink(0)
                m.getTile(x,y-1).setLink(2)
                self.visit(x,y-1,m)
            elif j[i] == 1 and (m.getTile(x+1,y) not in self.h.keys()) and m.getTile(x+1,y) != 0:
                m.getTile(x,y).setLink(1)
                m.getTile(x+1,y).setLink(3)
                self.visit(x+1,y,m)
            elif j[i] == 2 and (m.getTile(x,y+1) not in self.h.keys()) and m.getTile(x,y+1) != 0:
                m.getTile(x,y).setLink(2)
                m.getTile(x,y+1).setLink(0)
                self.visit(x,y+1,m)
            elif j[i] == 3 and (m.getTile(x-1,y) not in self.h.keys()) and m.getTile(x-1,y) != 0:
                m.getTile(x,y).setLink(3)
                m.getTile(x-1,y).setLink(1)
                self.visit(x-1,y,m)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    maker = MazeMaker()
                    maker.mazify(M)

        pygame.display.update()

main()