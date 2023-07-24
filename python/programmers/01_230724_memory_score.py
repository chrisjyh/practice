name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo =	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]


def solution(name, yearning, photo):
    answer = []
    memory = dict(zip(name, yearning))
    
    print(memory)

    for i in photo:
        result = 0
        for j in i:
            result += memory.get(j, 0)
        answer.append(result)
        result = 0

    
    return answer


print(solution(name, yearning, photo))