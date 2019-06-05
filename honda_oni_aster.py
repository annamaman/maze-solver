from module.text_analyzer import SquareTextAnalyzer
from module.maze import Maze
from module.aster_solver import AsterSolver
import pygame, sys, time
from pygame.locals import *
 
# 可変パラメータ
window_size = 600 #画面の大きさ
takeshi_current_loc = [0,0] #たけしのスタート位置
honda_current_loc = [17,19] #鬼のスタート位置
goal_loc = [19,19] #ゴールの位置
honda_speed = 100 #鬼のスピード 値の大きさに反比例して遅くなる

# pygameについての初期化、画像のロード、変形など
pygame.init()
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('honda_oni')
hondaImage = pygame.image.load('img/honda.jpg')
takeshiImage = pygame.image.load('img/takeshi.jpg')
winImage = pygame.image.load('img/win.jpg')
loseImage = pygame.image.load('img/Lose.jpg')
winImage = pygame.transform.scale(winImage,(600,300)) 
loseImage = pygame.transform.scale(loseImage,(600,300))

# 迷路の読み込みと画像サイズの調整など
analyzer = SquareTextAnalyzer("./map/honda_oni.txt")
maze = analyzer.text_to_list()
meiro_size = analyzer.get_text_size()
unit_size = window_size // meiro_size
hondaImage = pygame.transform.scale(hondaImage,(unit_size,unit_size))
takeshiImage = pygame.transform.scale(takeshiImage,(unit_size,unit_size))
font = pygame.font.Font(None, unit_size*165//100)
# pygame.mixer.init(frequency = 44100) 
# pygame.mixer.music.load("bgm/oni.mp3")
# pygame.mixer.music.play(-1) 

# プログラム中のみで使う変数
traj_index = 0
flame = 0
winFlg = False

# はじめの最短経路計算
maze_ = Maze(maze, [honda_current_loc[0],honda_current_loc[1]], [takeshi_current_loc[0],takeshi_current_loc[1]])
aster_solver = AsterSolver(maze_, [honda_current_loc[0],honda_current_loc[1]], [takeshi_current_loc[0],takeshi_current_loc[1]])
aster_solver.solve_maze()

# メインループ
while True:
    # 現在のフィールドの状況をblitで描写
    screen.fill((0,0,0))
    text = font.render("G", True, (255,255,255))   
    screen.blit(text, [goal_loc[0]*unit_size, goal_loc[1]*unit_size])
    for i in range(meiro_size):
        for j in range(meiro_size):
            if maze[i][j] == "W":
                pygame.draw.rect(screen,(0,150,0),Rect(j*unit_size, i*unit_size, unit_size, unit_size))                       
    screen.blit(takeshiImage, (takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size))
    screen.blit(hondaImage, (honda_current_loc[0]*unit_size, honda_current_loc[1]*unit_size))

    # イベント発生時の処理
    for event in pygame.event.get():    
        key_array = pygame.key.get_pressed()
        if key_array[273] == 1:#ue
            if takeshi_current_loc[1] != 0:
                if maze[takeshi_current_loc[1]-1][takeshi_current_loc[0]] == "S":           
                    pygame.draw.rect(screen,(0,0,0),Rect(takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size, unit_size, unit_size))
                    takeshi_current_loc[1] = takeshi_current_loc[1]-1
                    screen.blit(takeshiImage, (takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size))
                    maze_ = Maze(maze, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[1],takeshi_current_loc[0]])
                    aster_solver = AsterSolver(maze_, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[1],takeshi_current_loc[0]])
                    aster_solver.solve_maze()
                    traj_index = 0
        traj_index = traj_index + 1
        if key_array[274] == 1:#sita
            if takeshi_current_loc[1]+1 != meiro_size:
                if maze[takeshi_current_loc[1] +1][takeshi_current_loc[0]] == "S":          
                    pygame.draw.rect(screen,(0,0,0),Rect(takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size, unit_size, unit_size))
                    takeshi_current_loc[1]  = takeshi_current_loc[1] +1
                    screen.blit(takeshiImage, (takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size))
                    maze_ = Maze(maze, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[0],takeshi_current_loc[1]])
                    aster_solver = AsterSolver(maze_, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[1],takeshi_current_loc[0]])
                    aster_solver.solve_maze()
                    traj_index = 0
        if key_array[275] == 1:#migi
            if  takeshi_current_loc[0]+1 != meiro_size:
                if maze[takeshi_current_loc[1] ][takeshi_current_loc[0]+1] == "S":              
                    pygame.draw.rect(screen,(0,0,0),Rect(takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size, unit_size, unit_size))   
                    takeshi_current_loc[0] =  takeshi_current_loc[0]+1
                    screen.blit(takeshiImage, (takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size))
                    maze_ = Maze(maze, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[0],takeshi_current_loc[1]])
                    aster_solver = AsterSolver(maze_, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[1],takeshi_current_loc[0]])
                    aster_solver.solve_maze()
                    traj_index = 0
        if key_array[276] == 1:#hidari
            if  takeshi_current_loc[0] != 0:
                if maze[takeshi_current_loc[1]][takeshi_current_loc[0]-1] == "S":              
                    pygame.draw.rect(screen,(0,0,0),Rect(takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size, unit_size, unit_size))
                    takeshi_current_loc[0] =  takeshi_current_loc[0]-1
                    screen.blit(takeshiImage, (takeshi_current_loc[0]*unit_size, takeshi_current_loc[1]*unit_size))
                    maze_ = Maze(maze, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[0],takeshi_current_loc[1]])
                    aster_solver = AsterSolver(maze_, [honda_current_loc[1],honda_current_loc[0]], [takeshi_current_loc[1],takeshi_current_loc[0]])
                    aster_solver.solve_maze()
                    traj_index = 0        
        if takeshi_current_loc[0] == goal_loc[0] and takeshi_current_loc[1] == goal_loc[1]:
            screen.blit(winImage, (0,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,0,600,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,450,600,150))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # 本田鬼の位置を更新
    if flame % honda_speed == 0:
        honda_current_loc[0] =  aster_solver.shortest_route[traj_index][1]
        honda_current_loc[1] =  aster_solver.shortest_route[traj_index][0]
        if takeshi_current_loc[0] == honda_current_loc[0] and takeshi_current_loc[1] == honda_current_loc[1]:
            screen.blit(loseImage, (0,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,0,600,150))
            pygame.draw.rect(screen,(0,0,0),Rect(0,450,600,150))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        traj_index = traj_index + 1

    flame = flame + 1
    pygame.display.update()

