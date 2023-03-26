import sys

input = sys.stdin.readline

answer = 0
h, w = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(h + 1):
    
    l, r = -1, -1
    
    for j in range(w):
        
        if lst[j] >= i:
            if not l == -1:
                answer += r - l
                l = j
            else:
                l, r, = j, j
        r = j
        
print(answer)