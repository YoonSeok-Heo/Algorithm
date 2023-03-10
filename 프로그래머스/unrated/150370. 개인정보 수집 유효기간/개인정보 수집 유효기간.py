def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    terms_dic = {}
    for t in terms:
        a, b = t.split()
        terms_dic[a] = int(b)

    for i in range(len(privacies)):
        privacy = privacies[i].split()
        
        if (comp_day(today, add_day(privacy[0], terms_dic[privacy[1]]))):
            answer.append(i + 1)
    
    # print(add_day("2022.02.01", 3))
    return answer

def comp_day(today, privacy):
    print(today, privacy)
    for pair in zip(today, privacy):
        if pair[0] > pair[1]:
            return True
        elif pair[0] < pair[1]:
            return False
    return False

def add_day(privacy, term):
    
    privacy = list(map(int, privacy.split('.')))
    
    if privacy[2] == 1:
        term -= 1
    privacy[2] = (privacy[2] - 30) % 28 + 1
    
    
    privacy[0] += (privacy[1] + term - 1) // 12
    privacy[1] = (privacy[1] + term - 1) % 12 + 1
    
    return privacy