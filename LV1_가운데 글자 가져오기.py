def solution(s):
    answer = ''
    num = len(s)
    
    if num % 2 == 0:
        answer =  s[int((num/2)-1)]+s[int((num/2))]        
        return answer
    else:              
        return s[int((num-1)/2)]
