def count_button(n):
    if n%10 != 0:
        print(-1)
        return 0
    a, b, c = 300, 60, 10

    count = [0, 0, 0]
    while n > 0:
        if a <= n:
            count[0] += 1
            n -= a
        elif b <= n:
            count[1] += 1
            n -= b
        elif c<= n:
            count[2] += 1
            n -= c
      
    for c in count:
        print(c,end=" ")

n = int(input())
count_button(n)


