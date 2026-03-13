import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # 테스트케이스 개수

for _ in range(T):
    check = True
    left = True
    arr = deque([])
    functions = input() # 수행할 함수
    n = int(input()) # arr의 정수 개수
    nums = input()
    nums = list(map(int, nums.replace("[", "").replace("]", "").replace(",", " ").split()))

    for num in nums:
        arr.append(num)
    
    for i in range(len(functions)):
        if functions[i] == 'R':
            if left == True: left = False
            else: left = True
        elif functions[i] == 'D':
            if len(arr) == 0:
                print("error")
                check = False
                break
            if left == True: arr.popleft() # left=True일때 왼쩍에서 가장 첫번째거를 버림
            elif left == False: arr.pop()
    
    if len(arr) != 0:
        print('[',end='')
        if left == True:
            for i in range(len(arr)-1):
                print(arr.popleft(),end=',')
        elif left == False:
            for i in range(len(arr)-1):
                print(arr.pop(),end=',')

        print(arr.pop(),end='')
        print(']')
    elif len(arr) == 0 and check == True:
        print('[]')