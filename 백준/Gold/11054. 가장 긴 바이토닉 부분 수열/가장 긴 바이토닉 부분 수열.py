n = int(input())

lst = list(map(int, input().split()))
re_lst = lst[::-1]


dp = [1] * n
re_dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j] + 1, dp[i])
        
        if re_lst[i] > re_lst[j]:
            re_dp[i] = max(re_dp[j] + 1, re_dp[i])        

answer = [0] * n
for i in range(n):
    answer[i] = dp[i] + re_dp[n - i - 1] - 1

print(max(answer))