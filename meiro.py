import pygame, sys
from pygame.locals import *
import time
 

pygame.init()

screen = pygame.display.set_mode((600, 600))


pygame.display.set_caption('hondatomeiro')
peopleImage = pygame.image.load('people.jpg')
winImage = pygame.image.load('win.jpg')
winImage = pygame.transform.scale(winImage,(600,300)) 

def iter_chars(filename):
    """ Reads a text file char by char. """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    for ch in content:
        if ch == "\n":
            continue
        yield ch

def get_meiro_size(filename):
    meiro_size = 0
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    for ch in content:
        if ch == "\n":
            break
        meiro_size = meiro_size + 1
    return meiro_size

meiro_size = get_meiro_size('test.txt')
meiro = [["S" for i in range(meiro_size)] for j in range(meiro_size)]

i = 0
j = 0
for ch in iter_chars('test.txt'):
    if j == meiro_size:
        j = 0
        i = i + 1
    if ch == "W":
        meiro[i][j] = "W"
    j = j + 1

c = 600 // meiro_size

peopleImage = pygame.transform.scale(peopleImage,(c,c))

a = 0
b = 0

a_gall = 19
b_gall = 19

winFlg = False
font = pygame.font.Font(None, c*165//100)
       
while True: # main game loop
    screen.fill((0,0,0))
    text = font.render("G", True, (255,255,255))   
    screen.blit(text, [a_gall*c,b_gall*c])
    for i in range(meiro_size):
        for j in range(meiro_size):
                if meiro[i][j] == "W":
                    pygame.draw.rect(screen,(0,150,0),Rect(j*c,i*c,c,c))

            
            
    screen.blit(peopleImage, (a*c,b*c))
    if winFlg:
            time.sleep(2)
            pygame.quit()
            sys.exit()
    
    for event in pygame.event.get():
       
        key_array = pygame.key.get_pressed()
        if key_array[273] == 1:#ue
            if b != 0:
                if meiro[b-1][a] == "S":
                
                    pygame.draw.rect(screen,(0,0,0),Rect(a*c,b*c,c,c))
                    b = b-1
                    screen.blit(peopleImage, (a*c,b*c))
                
            
        if key_array[274] == 1:#sita
            if b+1 != meiro_size:
                if meiro[b+1][a] == "S":
                
                    pygame.draw.rect(screen,(0,0,0),Rect(a*c,b*c,c,c))
                    b = b+1
                    screen.blit(peopleImage, (a*c,b*c))
                

        if key_array[275] == 1:#migi
            if a+1 != meiro_size:
                if meiro[b][a+1] == "S":
               
                    pygame.draw.rect(screen,(0,0,0),Rect(a*c,b*c,c,c))   
                    a = a+1
                    screen.blit(peopleImage, (a*c,b*c))
                
        if key_array[276] == 1:#hidari
            if a != 0:
                if meiro[b][a-1] == "S":
                
                    pygame.draw.rect(screen,(0,0,0),Rect(a*c,b*c,c,c))
                    a = a-1
                    screen.blit(peopleImage, (a*c,b*c))
                
        if a == a_gall and b == b_gall:
            screen.blit(winImage, (0,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,0,600,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,450,600,150))
            winFlg = True

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()

