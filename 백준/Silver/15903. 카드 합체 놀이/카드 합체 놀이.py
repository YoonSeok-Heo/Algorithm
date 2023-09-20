import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

a, b = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))

heapify(cards)

for i in range(b):
    cardA, cardB = heappop(cards), heappop(cards)
    sumCards = cardA + cardB
    heappush(cards, sumCards)
    heappush(cards, sumCards)

print(sum(cards))