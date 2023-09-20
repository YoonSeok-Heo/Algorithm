import sys

input = sys.stdin.readline

m, n = map(int, input().split())

listA = list(list(map(int, input().strip())) for _ in range(m))

listB = list(list(map(int, input().strip())) for _ in range(m))

answer = 0

if (n < 3 or m < 3) and listA != listB:
    answer = -1
else:
    for i in range(m - 2):
        for j in range(n - 2):
            if listA[i][j] != listB[i][j]:
                answer += 1
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        listA[x][y] = 1 - listA[x][y]

if listA != listB:
    answer = -1
print(answer)