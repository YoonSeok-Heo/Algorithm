import sys
sys.setrecursionlimit(100000)

n = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer, colorWeek = 0, 0
visitBoard = [list(False for i in range(n)) for j in range(n)]
board = [list(input()) for i in range(n)]


def dfs(color, x, y):  
    global visitBoard

    visitBoard[x][y] = True

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
        if visitBoard[xx][yy] == False and board[xx][yy] == color:
            dfs(color, xx, yy)

for i in range(n):
    for j in range(n):
        if not visitBoard[i][j]:
            answer += 1
            dfs(board[i][j], i, j)
        if board[i][j] == 'G':
            board[i][j] = 'R'
            
visitBoard = [list(False for i in range(n)) for j in range(n)]

for i in range(n):
    for j in range(n):
        if not visitBoard[i][j]:
            colorWeek += 1
            dfs(board[i][j], i, j)

print(answer, colorWeek)

