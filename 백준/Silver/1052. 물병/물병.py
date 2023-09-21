n, k = map(int, input().split())

answer = n
while bin(n).count("1") > k:
    n += 1

print(n - answer)