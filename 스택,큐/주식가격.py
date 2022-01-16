def solution(prices):
    answers = []
    
    
    while prices:
        count = 0    
        for i in range(1, len(prices)):
            if prices[0] <= prices[i]:
                count += 1
            elif prices[0] > prices[i]:
                count += 1
                break
        if len(prices) == 1:
            answers.append(0)
        else:
            answers.append(count)
        prices.pop(0)
    
    return answers
