import pygame
import random
from random import randint
import tkinter as tk
WIDTH, HEIGHT = 500, 500
TILEWIDTH, TILEHEIGHT = 10, 10


window = tk.Tk()
window.title("Maze Engine")
window.geometry("300x100")

def inputCheck():
    input = str(entryField1.get())
    if int(input, 10) <= 0 or int(input,10) % 2 != 0:
       warning = tk.Label(text="Invalid input!")
       warning.grid(column=0,row=3)
       return
    else:
        global TILEWIDTH, TILEHEIGHT
        TILEWIDTH, TILEHEIGHT = int(input), int(input)
        window.destroy()
    return

#label
label = tk.Label(text="Enter size of square")
label.grid(column=0,row=0)

#entryfields
entryField1 = tk.Entry()
entryField1.grid(column=0,row=1)

#button
button1 = tk.Button(text="Generate Maze", command=inputCheck)
button1.grid(column=0,row=2)

window.mainloop()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Press Enter to Generate Maze')
pygame.init()


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
        #print('drawing ' + str(xcoor) + ' ' + str(ycoor) + ' ' + str(self.r) + str(self.g) + str(self.b) + str(self.links))
        pygame.draw.rect(WIN,(self.r,self.g,self.b),(xcoor,ycoor, WIDTH/TILEWIDTH, HEIGHT/TILEHEIGHT))
        if self.links[0] == 1:
            pygame.draw.line(WIN,(0,0,0),(xcoor,ycoor),(xcoor + (WIDTH/TILEWIDTH),ycoor), 2)
        if self.links[1] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor + (WIDTH/TILEWIDTH), ycoor), 2)
        if self.links[2] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor + (WIDTH/TILEWIDTH), ycoor + (HEIGHT/TILEHEIGHT)), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        if self.links[3] == 1:
            pygame.draw.line(WIN, (0, 0, 0), (xcoor, ycoor), (xcoor, ycoor + (HEIGHT/TILEHEIGHT)), 2)
        pygame.display.update()
        return

    def setLink(self,n):
        self.links[n] = 0

    def setRGB(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def resetLinks(self):
        self.links = [0,1,2,3]

class Maze:
    tiles = []
    links = []
    def reset(self):
        for i in range(len(self.tiles)):
            for j in self.tiles[i]:
                j.setRGB(randint(0,255),randint(0,255), randint(0,255))
                j.resetLinks()


    def __init__(self,w,h):
        links = []
        tiles = []
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
        #print('72')
        #print('setting ' + str(x) + ' ' + str(y))
        self.tiles[y][x].setRGB(r,g,b)
        self.tiles[y][x].draw()

    def getTile(self,x,y):
        if x < 0 or y < 0 or x >= TILEWIDTH or y >= TILEHEIGHT:
            return 0
        return self.tiles[y][x]

class MazeMaker:
    h = {}
    def __init__(self):
        self.h = {}

    def mazify(self, m):
        self.visit(0,0,m)

    def visit(self,x,y,m):
        #print('VISITING ' + str(x) + ' ' + str(y))
        if m.getTile(x,y) == 0:
            #print('invalid')
            return
        m.set(x,y,255,255,255)
        self.h[m.getTile(x,y)] = randint(0,1000)
        j = list(range(4))
        random.shuffle(j)
        for i in j:
            #print('199')
            if j[i] == 0 and (m.getTile(x,y-1) not in self.h.keys()) and m.getTile(x,y-1) != 0:
                #print('linking ' + str(x) + str(y) + ' and ' + str(x) + str(y-1))
                m.getTile(x,y).setLink(0)
                m.getTile(x,y-1).setLink(2)
                m.draw()
                self.visit(x,y-1,m)
            elif j[i] == 1 and (m.getTile(x+1,y) not in self.h.keys()) and m.getTile(x+1,y) != 0:
                #print('linking ' + str(x) + str(y) + ' and ' + str(x+1) + str(y))
                m.getTile(x,y).setLink(1)
                m.getTile(x+1,y).setLink(3)
                m.draw()
                self.visit(x+1,y,m)
            elif j[i] == 2 and (m.getTile(x,y+1) not in self.h.keys()) and m.getTile(x,y+1) != 0:
                #print('linking ' + str(x) + str(y) + ' and ' + str(x) + str(y+1))
                m.getTile(x,y).setLink(2)
                m.getTile(x,y+1).setLink(0)
                m.draw()
                self.visit(x,y+1,m)
            elif j[i] == 3 and (m.getTile(x-1,y) not in self.h.keys()) and m.getTile(x-1,y) != 0:
                #print('linking ' + str(x) + str(y) + ' and ' + str(x-1) + str(y))
                m.getTile(x,y).setLink(3)
                m.getTile(x-1,y).setLink(1)
                m.draw()
                self.visit(x-1,y,m)


def main():

    run = True
    FPS = 120
    clock = pygame.time.Clock()
    #print('HERE')
    M = [Maze(TILEWIDTH, TILEHEIGHT)]
    #print('134')
    M[0].draw()
    makers = [MazeMaker()]
    num = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    maker = makers[num]
                    maker.mazify(M[0])
                    M.pop(0)
        pygame.display.update()
window.mainloop()
main()
