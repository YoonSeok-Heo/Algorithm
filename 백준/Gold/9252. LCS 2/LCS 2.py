import sys

input = sys.stdin.readline

n, m = input().strip(), input().strip()

lenn, lenm = len(n), len(m)

dp = list([""] * (lenm + 1) for i in range(lenn + 1))

for i in range(1, lenn + 1):
	for j in range(1, lenm + 1):
		if n[i - 1] == m[j - 1]:
			dp[i][j] = dp[i - 1][j - 1] + n[i - 1]
		else:
			if (len(dp[i - 1][j]) >= len(dp[i][j - 1])):
				dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i][j - 1]

print(len(dp[lenn][lenm]))
print(dp[lenn][lenm])