import sys

input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                
print(max(dp))
answer = []