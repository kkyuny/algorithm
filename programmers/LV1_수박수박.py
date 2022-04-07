def solution(n):
    answer = ''
    for m in range(n):
        if m % 2 == 0:
            answer += '수'
        elif m % 2 == 1:
            answer += '박'
    return answer
