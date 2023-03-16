import sys
n, m = map(int, input().split(' '))
lan = [0] * n
for i in range(n):
    lan[i] = int(sys.stdin.readline())
left, right = 1, max(lan)
while left <= right:
    mid = (left + right) // 2
    count_lan = 0
    for l in lan:
        count_lan += l // mid
    if count_lan >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)