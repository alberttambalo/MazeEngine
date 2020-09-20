import pygame
import time
import random
from random import randint
import math


pygame.init()

WIDTH, HEIGHT = 500, 500
TILEWIDTH, TILEHEIGHT = 100, 100
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
class Tile:
    def __init__(self,x,y,r,g,b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.links = [0,0,0,0]

    def draw(self):
        pygame.draw.rect(WIN,(self.r,self.g,self.b),(self.x * (WIDTH/TILEWIDTH),self.y * (HEIGHT/TILEHEIGHT), WIDTH/TILEWIDTH, HEIGHT/TILEHEIGHT))
        for i in range(4):
            if self.links[i] == 0:
                pygame.draw.line(WIN,(255,255,255),(self.x,self.y),(self.x + (WIDTH/TILEWIDTH),self.y), 5)
            if self.links[i] == 1:
                pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x + (WIDTH / TILEWIDTH), self.y), 5)
            if self.links[i] == 2:
                pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x + (WIDTH / TILEWIDTH), self.y), 5)
            if self.links[i] == 3:
                pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x, self.y + (HEIGHT/TILEHEIGHT)), 5)

        return

class Maze:
    tiles = []
    def __init__(self,w,h):
        for i in range(w):
            temp = []
            for j in range(h):
                temp.append(Tile(j,i,0,0,0))
            self.tiles.append(temp)

    def draw(self):
        for i in self.tiles:
            for j in i:
                j.draw()
        for i in self.tiles:
            for j in range(4):


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