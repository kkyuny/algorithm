def solution(phone_number):
    a = (len(phone_number) - 4) * "*"
    b = phone_number[-4:]     
    return a + b     
