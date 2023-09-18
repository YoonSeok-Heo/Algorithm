import sys

input = sys.stdin.readline

alphaList = [0 for i in range(26)]

for i in range(int(input())):

    word = list(input().strip())
    count = 0
    for alpha in word[::-1]:
        # print(alpha)
        alphaList[ord(alpha) - 65] += 10 ** count
        count += 1
# print(alphaList)
answer = 0
count = 9
alphaList.sort(reverse=True)

for i in alphaList:
    answer += count * i
    count -= 1

# print(alphaList)
print(answer)
