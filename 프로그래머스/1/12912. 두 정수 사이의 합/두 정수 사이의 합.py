def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    
    high = max(a,b)
    low = min(a,b)
    while low <= high:
        answer += low
        low += 1
    return answer