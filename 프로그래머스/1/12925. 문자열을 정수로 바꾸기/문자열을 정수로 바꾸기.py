def solution(s):
    if s[0] == "-":
        num = s[1:]
        answer = int(num)
        answer *= -1
    elif s[0] == "+":
        num = s[1:]
        answer = int(num)
    else: answer = int(s)
    
    return answer