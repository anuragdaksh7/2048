import pygame
import math
import random
from tileDraw import *
from moveDown import *
from moveUp import *
from moveRight import *
from moveLeft import *
from drawGrid import *
from createNewBlock import *

# 4x4 grid
# arrow keys

grid = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
]
while sum([grid[i].count(0) for i in range(4)])>14:
	x,y = random.randint(0,3),random.randint(0,3)
	# print(x,y)
	grid[x][y] = random.choice([2,2,2,2,2,2,4])
	# print(grid)


def check_end(grid):
	if sum([grid[i].count(0) for i in range(4)]) >0:
		return False
	end = True
	for i in range(3):
		for j in range(3):
			if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
				# print(i,j,grid[i][j])
				end = False
	return end


def draw_grid(grid):
	c = 10
	for i in range(4):
		for j in range(4):
			pygame.draw.rect(win, (205,193,180), (i*150+c, j*150+c, 150 - 2*c, 150 - 2*c), 0)
			if grid[i][j]!= 0:
				draw_num(grid[i][j],[i,j],font, win)

pygame.init()

win = pygame.display.set_mode((600,600))
font = pygame.font.Font(None, 60)  # Use the default font with a size of 36

run = True
while run:
	pygame.time.delay(1000//10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill((186,172,160))
	k = 0
	# if pygame.mouse.get_pressed()[0] and k == 0:
	# 	k = 1
	# 	mov_left(grid)
	# if pygame.mouse.get_pressed()[2] and k == 0:
	# 	k = 1
	# 	mov_down(grid)

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_RIGHT]:
		s = list(grid)
		mov_right(grid)
		createNewBlock(grid)
	if pressed[pygame.K_LEFT]:
		s = list(grid)
		mov_left(grid)
		createNewBlock(grid)
	if pressed[pygame.K_UP]:
		s = list(grid)
		mov_up(grid)
		createNewBlock(grid)
	if pressed[pygame.K_DOWN]:
		s = list(grid)
		mov_down(grid)
		createNewBlock(grid)
	draw_grid(grid)
	pygame.display.update()
pygame.quit()