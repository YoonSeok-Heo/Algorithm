import sys
import heapq

input = sys.stdin.readline

class_list = []

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    class_list.append([a, b])

class_list.sort()

h = []
heapq.heappush(h, class_list[0][1])

for i in range(1, n):
    if class_list[i][0] >= h[0]:
        heapq.heappop(h)
    heapq.heappush(h, class_list[i][1])

print(len(h))