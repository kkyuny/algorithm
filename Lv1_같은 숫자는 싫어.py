def solution(arrs):
    answer = []
    answer.append(arrs[0])
    for arr in range(1, len(arrs)):        
        if arrs[arr-1] != arrs[arr]:            
            answer.append(arrs[arr])        
    return answer
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
