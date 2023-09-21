import sys

input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())
    lst = list(map(int, input().strip().split()))

    max_val = 0
    answer = 0

    for i in range(len(lst) - 1, -1, -1):
        if max_val < lst[i]:
            max_val = lst[i]
        else:
            answer += max_val - lst[i]

    print(answer)

