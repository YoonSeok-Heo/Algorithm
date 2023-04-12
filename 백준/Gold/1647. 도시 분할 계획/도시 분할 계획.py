import sys

input = sys.stdin.readline
edges = []
maxd, count, answer = 0, 0, 0
n, m = map(int, input().split())
union = list(i for i in range(n + 1))

def find_parent(x):
	global union
	if union[x] != x:
		union[x] = find_parent(union[x])
	return union[x]

def union_parent(a, b):
	global union
	a = find_parent(a)
	b = find_parent(b)
	if a < b:
		union[b] = a
	else:
		union[a] = b
	
for i in range(m):
	a, b, c = map(int, input().strip().split())
	edges.append((c, a, b))	

edges.sort()

for cost, a, b in edges:
	
	if find_parent(a) != find_parent(b):
		union_parent(a, b)
		answer += cost
		count += 1
		if count + 1 >= n:
			break
		
# print(cost)
# print(union)
# print(edges)
print(answer - cost)