import sys
sys.setrecursionlimit(10** 6)

input = sys.stdin.readline
lst = []

while True:
    try:
        lst.append(int(input()))
    except:
        break

def postorder(s, e):
    if s > e:
        return
    
    mid = e + 1
    for i in range(s + 1, e + 1):
        if lst[i] > lst[s]:
            mid = i
            break
        
    postorder(s + 1, mid - 1)
    postorder(mid, e)
    print(lst[s])

postorder(0, len(lst) - 1)
