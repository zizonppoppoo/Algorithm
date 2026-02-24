import sys
input = sys.stdin.readline

T = int(input())
arr = [[0,0] for _ in range(41)]
check = [False] * 41
arr[0] = [1,0]
arr[1] = [0,1]
check[0] = True
check[1] = True
for _ in range(T):
    x = int(input())
    for i in range(2,x+1):
        if check[i] == False:
            check[i] = True
            arr[i][0] = arr[i-1][0] + arr[i-2][0]
            arr[i][1] = arr[i-1][1] + arr[i-2][1]
    print(arr[x][0], arr[x][1])