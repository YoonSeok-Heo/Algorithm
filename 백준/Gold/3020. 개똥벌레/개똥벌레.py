import sys

input = sys.stdin.readline

n, h = map(int, input().split())
a_arr, b_arr = [], []
min_answer, result = n, 0

def binary_search(start, end, arr, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

for i in range(n // 2):
    a_arr.append(int(input()))
    b_arr.append(h - int(input()))
    
a_arr.sort()
b_arr.sort()


for i in range(h):
    r1 = n // 2 - binary_search(0, n // 2, a_arr, i)
    r2 = binary_search(0, n // 2, b_arr, i)
    
    total = r1 + r2 # (총 닿은 면 개수)
    if min_answer == total:
        result += 1
    elif min_answer > total:
        min_answer = total
        result = 1

print(min_answer, result)
