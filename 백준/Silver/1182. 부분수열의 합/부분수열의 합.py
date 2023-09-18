n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
answer = 0

def dfs(s, p):
    global answer
    if p >= n:
        return
    s += lst[p]
    if s == m:
        answer += 1
    dfs(s - lst[p], p + 1)
    dfs(s, p + 1)
dfs(0, 0)

print(answer)