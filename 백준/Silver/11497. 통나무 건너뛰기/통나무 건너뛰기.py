import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):

    n = int(input().strip())

    lst = list(map(int, input().split()))

    lst.sort()
    
    answer = 0
    for j in range(2, n):
        answer = max(answer, abs(lst[j] - lst[j - 2]))
    
    print(answer)