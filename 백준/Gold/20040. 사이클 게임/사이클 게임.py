import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

parent = list(i for i in range(n))

def find(p, x):
	if p[x] != x:
		return find(p, p[x])
	return p[x]
	
def union(p, x, y):
	x = find(p, x)
	y = find(p, y)
	
	if x == y:
		return True
	
	if x < y:
		p[y] = x
	else:
		p[x] = y
	
	return False

for i in range(m):
	a, b = map(int, input().split())
	
	if union(parent, a, b):
		print(i + 1)
		exit()
print(0)
	
	


