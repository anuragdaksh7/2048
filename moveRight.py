def mov_right(grid):
	for i in range(4):
		k = []
		for j in range(4):
			k.append(grid[j][i])
		if (k.count(0) == 4):
			continue
		c = 3
		# k = grid[i]
		print("k",k)
		l = []
		for j in k:
			if j:
				l.append(j)
		# print(l)
		t = []
		k = len(l)-1
		while len(l):
			# print(k,l,t)
			if l[k] == l[k-1] and k>=1:
				t.append(l[k]*2)
				try:
					l.pop()
					l.pop()
				except:
					None
				k-=2
			else:
				t.append(l[k])
				l.pop()
				k-=1
		while len(t)!=4:
			t.append(0)
		t = t[::-1]
		print(t)
		for j in range(4):
			grid[j][i] = t[j]