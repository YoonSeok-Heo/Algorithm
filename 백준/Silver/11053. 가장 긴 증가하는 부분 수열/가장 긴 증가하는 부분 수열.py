n = int(input())
dp = list(map(int, input().split()))
answer = [0] * (n + 1)

for i in range(n):
    minNum = 0
    for j in range(i + 1):
        if dp[i] > dp[j]:
            if minNum < answer[j]:
                minNum = answer[j]
    answer[i] = minNum + 1
    



print(max(answer))