def solution(seoul):
    answer = ''
    ind = 0
    for ksb in seoul:            
        if(ksb == "Kim"):            
            answer = "김서방은 {}에 있다".format(ind)
            return answer
        ind += 1
