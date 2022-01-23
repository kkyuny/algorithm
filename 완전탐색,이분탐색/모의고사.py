def solution(answers):
    num1 = []
    num2 = []
    num3 = []
    result = [0,0,0]
    for i in range(len(answers)):
        # num1 에 원소 추가
        num1.append((i%5+1)) 
        
        # num2에 원소 추가
        if i % 2 == 0: 
            num2.append(2)
        else:
            if i % 8 == 1:
                num2.append(1)
            elif i % 8 == 3:
                num2.append(3)
            elif i % 8 == 5:
                num2.append(4)
            elif i % 8 == 7:
                num2.append(5)
        
        # num3에 원소 추가
        if i % 10 == 0 or i % 10 == 1:
            num3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            num3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            num3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            num3.append(4)
        elif i % 10 == 8 or i % 10 == 9:
            num3.append(5)
        
        # 결과값 비교
        if answers[i] == num1[-1]:
            result[0] += 1
        if answers[i] == num2[-1]:
            result[1] += 1
        if answers[i] == num3[-1]:
            result[2] += 1
    print(num1, num2, num3)
    #결과값 리턴
    results = []
    maxValue = max(result)
    for i in range(len(result)):
        if maxValue == result[i]:
            results.append(i+1)   
        
    return results
