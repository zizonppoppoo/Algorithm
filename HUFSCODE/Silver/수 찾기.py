import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split())) # 존재하는 정수 모임
M = int(input())
find_list = list(map(int, input().split())) # 찾아야하는 정수 모임

numbers.sort() # 이진탐색 사용하기 위해 정렬

def binary_search(start, end, x):
    if start > end: return 0

    pivot = (start + end) // 2
    num = numbers[pivot]

    if num == x: return 1
    elif num < x: return binary_search(pivot+1, end, x)
    else: return binary_search(start, pivot-1, x)

for x in find_list:
    print(binary_search(0, N-1, x))