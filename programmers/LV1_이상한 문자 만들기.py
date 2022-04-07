def solution(s):
    answer = ''
    i = 0
    words = s.split(" ")
    for word in words:
        for w in word:            
            if i % 2 == 0:
                w = w.upper()
                answer += w
            else:
                w = w.lower()
                answer += w
            i += 1       
        answer += " "
        i = 0
    return answer[:-1]
