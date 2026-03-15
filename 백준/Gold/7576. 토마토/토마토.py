import sys
from collections import deque
input = sys.stdin.readline

def check(M,N):
    max = 0
    for n in range(N):
        for m in range(M):
            if box[n][m] == -2: return -1
            elif box[n][m] > max: max = box[n][m]
    return max

moveX = [-1,0,1,0]
moveY = [0,1,0,-1]
M, N = map(int,input().split())
box = [[-2 for _ in range(M)] for _ in range(N)]
red_tomato = []
check_zero = False

for n in range(N):
    info = list(map(int,input().split()))
    for m in range(M):
        if info[m] == 1:
            red_tomato.append((m,n))
            box[n][m] = 0
        elif info[m] == -1:
            box[n][m] = -1
        else:
            check_zero = True

if check_zero == False:
    print(0)
else:
    queue = deque([])
    for nums in red_tomato:
        queue.append(nums)
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nextX = x + moveX[i]
            nextY = y + moveY[i]
            if 0 <= nextX < M and 0 <= nextY < N and box[nextY][nextX] == -2:
                box[nextY][nextX] = box[y][x] + 1
                queue.append((nextX,nextY))
    print(check(M,N))