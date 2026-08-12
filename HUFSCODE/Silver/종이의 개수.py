import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def prime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False

    i = 3
    while i*i <= num:
        if num % i == 0: return False
        i += 2

    return True

result = []

for num in range(N, M+1, 1):
    if prime(num): result.append(num)

if len(result) == 0: print(-1)
else:
    result_sum = 0
    for num in result:
        result_sum += num

    print(result_sum)
    print(result[0])