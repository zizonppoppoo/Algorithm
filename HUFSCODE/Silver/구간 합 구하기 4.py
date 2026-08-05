import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 수의 개수, M : 정답 개수
nums = list(map(int, input().split()))
numbers = [0]

for i in range(N):
    numbers.append(numbers[i]+nums[i])

for _ in range(M):
    x, y = map(int, input().split())
    print(numbers[y] - numbers[x-1])