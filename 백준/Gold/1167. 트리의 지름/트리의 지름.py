from collections import deque

v = int(input())

graph = {i: [] for i in range(1, v + 1)}

for i in range(1, v + 1):
	arr = list(map(int, input().split()))
	
	for i in range(1, len(arr) // 2):
		graph[arr[0]].append([arr[i * 2 - 1], arr[i * 2]])


q = deque()
q.append([1, 0])

visit = [0] * (v + 1)
visit[1] = 1
max_n, max_w = 1, 0

while q:
	
	n, w = q.popleft()
	if max_w < w:
		max_n = n
		max_w = w
	
	for nn, nw in graph[n]:
		
		if visit[nn]:
			continue
		q.append([nn, nw + w])
		visit[nn] = 1


q = deque()
q.append([max_n, 0])

visit = [0] * (v + 1)
visit[max_n] = 1
max_n, max_w = max_n, 0

while q:
	
	n, w = q.popleft()
	if max_w < w:
		max_n = n
		max_w = w
	
	for nn, nw in graph[n]:
		
		if visit[nn]:
			continue
		q.append([nn, nw + w])
		visit[nn] = 1

print(max_w)

