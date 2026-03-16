import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)
arr.sort()
for i in arr:
    print(i)