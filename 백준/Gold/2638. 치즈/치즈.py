import sys

input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

N, M = map(int, input().split())

lst = list(list(map(int, input().split())) for i in range(N))

def dfs(x, y):
	global lst
	
	tmp = list([0] * M for i in range(N))
	visit = list([0] * M for i in range(N))
	
	stack = [[x, y]]
	while stack:
		
		x, y = stack.pop()
		
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]

			
			if 0 > nx or N <= nx or 0 > ny or M <= ny:
				continue
			
			if visit[nx][ny] == 1:
				continue
				
			if lst[nx][ny] == 1:
				tmp[nx][ny] += 1
				
			if lst[nx][ny] == 0:
				visit[nx][ny] = 1
				stack.append([nx, ny])
	ret_type = False
	for i in range(N):
		for j in range(M):
			if tmp[i][j] > 1:
				ret_type = True
				lst[i][j] = 0
				
	# for t in tmp:
	# 	print(t)
	# print()
	
	return ret_type
	
	
	
count = 0
while(dfs(0, 0)):
	count += 1
	
print(count)


# for l in lst:
# 	print(l)