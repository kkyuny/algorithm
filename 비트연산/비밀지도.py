def make_base(n, base):
    q = n // base
    r = str(n % base)
    
    if q == 0:
        return r
    else:
        return make_base(q, base) + r

def solution(n, arr1, arr2):
    
    result = []
    by_arr1 = []
    by_arr2 = []
    for i in range(n):
        by_arr1.append(make_base(arr1[i],2).rjust(n,'0'))
        by_arr2.append(make_base(arr2[i],2).rjust(n,'0'))    
    
    for i in range(n):
        answer = []
        for j in range(n):            
            if ((int(by_arr1[i][j]) == 0) and ((int(by_arr2[i][j]) == 0))):
                answer.append(" ")                       
            else:
                answer.append("#")                            
        result.append(''.join(answer))
    
    return result
