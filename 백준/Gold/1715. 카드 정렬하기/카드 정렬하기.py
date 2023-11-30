import sys
import heapq
heap = []
n = int(input())
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

sumTmp = 0
sumTmp2 = 0
for _ in range(n - 1):
    sumTmp = heapq.heappop(heap) + heapq.heappop(heap)
    sumTmp2 += sumTmp
    heapq.heappush(heap, sumTmp)

print(sumTmp2)
