def solution(progresses, speeds):
    answer = []  
       
    i = 0    
    while progresses:    
        l = 0        
        for a in range(len(progresses)):
            if progresses[a] < 100:
                progresses[a] += speeds[a]                
        
        print(progresses)

        while progresses[0] >= 100:                       
            progresses.pop(0)
            speeds.pop(0)                
            l += 1

            if len(progresses) == 0:
                answer.append(l)
                break                     
            elif progresses[0] < 100:
                answer.append(l)
                break       

        print(answer)                     
                                              
    return answer
