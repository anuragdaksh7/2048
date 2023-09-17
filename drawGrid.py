import pygame
pygame.init()

def draw_grid(grid, win):
	c = 10
	for i in range(4):
		for j in range(4):
			pygame.draw.rect(win, (205,193,180), (i*150+c, j*150+c, 150 - 2*c, 150 - 2*c), 0)
			if grid[i][j]!= 0:
				draw_num(grid[i][j],[i,j],font, win)