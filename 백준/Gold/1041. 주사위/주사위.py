N = int(input())

dice = [0] + list(map(int, input().split()))

if N == 1:
    print(sum(sorted(dice)[:-1]))
else:
    
    answer = 0

    min_val = min(dice[1:])
    three_min = min(dice[1] + dice[2] + dice[3], dice[1] + dice[2] + dice[4], dice[1] + dice[4] + dice[5], dice[1] + dice[5] + dice[3], dice[6] + dice[2] + dice[3], dice[6] + dice[2] + dice[4], dice[6] + dice[4] + dice[5], dice[6] + dice[5] + dice[3])
    two_min = min(dice[1] + dice[2], dice[1] + dice[3], dice[1] + dice[4], dice[1] + dice[5], dice[2] + dice[3], dice[2] + dice[4], dice[2] + dice[6], dice[3] + dice[5], dice[3] + dice[6], dice[4] + dice[5], dice[4] + dice[6], dice[5] + dice[6])


    answer = (three_min * 4) + ((N - 2) * two_min  * 4) + ((N - 1) * two_min * 4) + ((N - 1) * (N - 2) * 4 * min_val) + (((N - 2) ** 2) * min_val)

    print(answer)