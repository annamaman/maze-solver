import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + './module')

# A*アルゴリズムにより迷路の最短経路を計算
from text_analyzer import SquareTextAnalyzer
from maze import Maze
from aster_solver import AsterSolver

start_point = [0,0]
goal_point = [19,19]
analyzer = SquareTextAnalyzer("./map/test.txt")
maze = analyzer.text_to_list()
maze = Maze(maze, start_point, goal_point)

aster_solver = AsterSolver(maze, start_point, goal_point)
aster_solver.solve_maze()

# 最短経路をpygameを用いて本田が動くように表示
import pygame
from pygame.locals import *
import time

pygame.init()

meiro_size = analyzer.get_text_size()
c = 600 // meiro_size

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('./img/hondatomeiro')
peopleImage = pygame.image.load('./img/people.jpg')
peopleImage = pygame.transform.scale(peopleImage,(c,c))
winImage = pygame.image.load('./img/win.jpg')
winImage = pygame.transform.scale(winImage,(600,300))
font = pygame.font.Font(None, c*165//100)

while True:
    screen.fill((0,0,0))
    text = font.render("G", True, (255,255,255))   
    screen.blit(text, [goal_point[1]*c, goal_point[0]*c])
    for i in range(meiro_size):
        for j in range(meiro_size):
                if maze.maze[i][j] == "W":
                    pygame.draw.rect(screen,(0,150,0),Rect(j*c,i*c,c,c))           
    
    for traje in aster_solver.shortest_route:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(peopleImage, (traje[1]*c,traje[0]*c))
        time.sleep(0.5)
        pygame.display.update()

        if traje[0] == goal_point[0] and traje[1] == goal_point[1]:
            screen.blit(winImage, (0,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,0,600,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,450,600,150))
            pygame.display.update()
            time.sleep(0.2)
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen,(0,0,0),Rect(traje[1]*c,traje[0]*c,c,c))
