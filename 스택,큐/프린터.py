def solution(priorities, location):
    
    answer = 0
    idx = [i for i in range(len(priorities))]
    while priorities:        
        count = 0
        i = idx.pop(0)
        j = priorities.pop(0)
        count += 1
        for p in range(len(priorities)):
            if j < priorities[p]:
                priorities.append(j)
                idx.append(i)
                count -= 1
                break
        if count == 1:
            answer += 1
            if i == location:
                return answer        
    return answer
