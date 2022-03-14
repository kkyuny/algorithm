def solution(n, lost, reserve):
    students = [1 for _ in range(n)]
    
    for i in lost:
        students[i-1] -= 1
    for i in reserve:
        students[i-1] += 1           
    
    if students[0] == 2:
        if students[1] == 0:
            students[0] -= 1
            students[1] += 1            
    
    for i in range(1,len(students)-1):
        if students[i]==2:
            if students[i-1]==0:
                students[i-1] += 1
                students[i] -= 1
            elif students[i+1]==0:
                students[i+1] += 1
                students[i] -= 1    
    
    if students[-1] == 2:
        if students[-2] == 0:
            students[-1] -= 1
            students[-2] += 1
    print(students)
    answer = 0
    for student in students:
        if student >= 1:
            answer += 1
    
    return answer
