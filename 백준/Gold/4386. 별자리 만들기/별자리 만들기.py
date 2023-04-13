import sys

input = sys.stdin.readline

n = int(input().strip())

lst = []
dis = []
parent = list(i for i in range(n))
count, answer = 0, 0

def find(p, x):
	if p[x] != x:
		return find(p, p[x])
	return p[x]

def union(p, x, y):
	x = find(p, x)
	y = find(p, y)
	
	if x == y:
		return False
	
	if x < y:
		p[y] = x
	elif x > y:
		p[x] = y
	
	return True

def calc(ax, ay, bx, by):
	x = abs(ax - bx)
	y = abs(ay - by)
	ans = (x ** 2 + y ** 2) ** 0.5
	return ans
	
for i in range(n):
	a, b = map(float, input().split())
	lst.append((a, b))
	
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		dis.append((calc(lst[i][0], lst[i][1], lst[j][0], lst[j][1]), i, j))
dis.sort()
		
for i in range(len(dis)):
	
	if union(parent, dis[i][1], dis[i][2]):
		count += 1
		answer += dis[i][0]

print("%.2f"%answer)