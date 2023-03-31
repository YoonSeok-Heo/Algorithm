import sys
import bisect

INF = (10 ** 10)

input = sys.stdin.readline

N = int(input())

lst = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
nums = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                nums[i] = lst[i]
            else:
                dp[i] = dp[i]
                nums[i] = lst[i]
                
maxCount = max(dp)
print(maxCount)
answer = []
for i in range(N, 0, -1):
    if dp[i] == maxCount:
        answer.append(nums[i])
        maxCount -= 1

print(*answer[::-1])