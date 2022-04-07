def solution(s):
    words = s.lower()
    p_count = 0
    y_count = 0
    for word in words:
        if word == "p":
            p_count += 1
        elif word == "y":
            y_count += 1
    if p_count == y_count:
        return True
    else:
        return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
