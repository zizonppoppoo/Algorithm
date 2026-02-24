import sys
input = sys.stdin.readline
T = int(input())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(T):
    index = 4
    x = int(input())
    while arr[x] == 0:
        arr[index] = arr[index-1] + arr[index-2] + arr[index-3]
        index += 1
    print(arr[x])