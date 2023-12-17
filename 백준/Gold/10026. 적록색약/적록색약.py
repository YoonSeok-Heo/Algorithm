from sys import stdin

input = stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

answer, color_answer = 0, 0

n = int(input())
arr = [list(input()) for i in range(n)]

def dfs(color, x, y):
    
    global visit
    s = [[x, y]]
    
    while s:
        
        xx, yy = s.pop()
        
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if arr[nx][ny] == color:
                visit[nx][ny] = True
                s.append([nx, ny])
                
            
visit = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            answer += 1
            visit[i][j] = True
            dfs(arr[i][j], i, j)
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
            
visit = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            color_answer += 1
            visit[i][j] = True
            dfs(arr[i][j], i, j)
    

print(answer, color_answer)
