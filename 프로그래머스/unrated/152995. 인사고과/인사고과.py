def solution(scores):
    answer = 1

    wanho = scores[0]
    sum_wanho = sum(wanho)

    scores.sort(key = lambda s: (-s[0], s[1]))

    max_score = 0



    for s in scores:
        if wanho[0] < s[0] and  wanho[1] < s[1]:
            return -1
        if max_score <= s[1]:
            if sum_wanho < s[0] + s[1]:
                answer += 1
            max_score = s[1]
    return answer
