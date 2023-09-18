from random import choice

def createNewBlock(grid):
	a = []
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				a.append([i,j])
	if len(a) == 0:
		return
	x,y = choice(a)
	grid[x][y] = choice([2,2,2,2,2,2,4])