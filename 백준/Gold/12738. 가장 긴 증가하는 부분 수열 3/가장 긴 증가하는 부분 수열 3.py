import sys
import bisect

INF = (10 ** 10)

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

dp = [INF] * N

for i in lst:
	pos = bisect.bisect_left(dp, i)
	dp[pos] = i
	
count = 0
for i in dp:
	if i == INF:
		break
	count += 1
print(count)