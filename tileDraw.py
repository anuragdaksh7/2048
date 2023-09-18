import pygame
import math
pygame.init()

def draw_num(n, pos, font, win):
	x, y = pos
	# print(x,y,n)
	if n == 2:
		text = "2"
		text_surface = font.render(text, True, (120,110,103))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (238,229,219), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n == 4:
		text = "4"
		text_surface = font.render(text, True, (120,110,103))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (239,225,200), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n == 8:
		text = "8"
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (243,178,122), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n == 16:
		text = "16"
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (246,151,101), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n == 32:
		text = "32"
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (247,125,94), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n == 64:
		text = "64"
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (247,95,59), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n >= 128:
		text = str(n)
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (236,208,114), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)

	if n>2048:
		text = str(n)
		text_surface = font.render(text, True, (248,247,242))
		text_rect = text_surface.get_rect()
		text_rect.center = (150*x+75, 150*y+75)
		c = 10
		pygame.draw.rect(win, (0,0,0), (x*150+c, y*150+c, 150 - 2*c, 150 - 2*c), 0)
		win.blit(text_surface, text_rect)
