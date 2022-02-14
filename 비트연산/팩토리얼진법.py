import math

while True:
    n = int(input().strip())
    sum = 0
    idx = 1

    if n == 0:        
        break       
    while n >= 1:
        if n%10 == 0:
            sum += 0;
        else:
            sum += (n%10)*(math.factorial(idx))
        n //= 10
        idx += 1               
    print(sum)
