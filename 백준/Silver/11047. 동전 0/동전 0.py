n, money = map(int, input().split())
coin = list()
count = 0
for i in range(n):
    coin.append(int(input()))
coin.reverse()
for i in coin:
    div = money // i
    money -= div * i
    count += div
print(count)
