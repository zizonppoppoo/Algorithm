import sys
from collections import deque
input = sys.stdin.readline

def check(M,N,H):
    max = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if result[h][n][m] == -2: return -1
                elif result[h][n][m] != -1:
                    if max < result[h][n][m]: max = result[h][n][m]
    return max


M, N, H = map(int,input().split()) # 차례대로 가로,세로,높이
box = [[None for _ in range(N)] for _ in range(H)]
result = [[[-2 for _ in range(M)] for _ in range(N)] for _ in range(H)]
red_tomato = []
check_zero = False

moveX = [-1,0,1,0]
moveY = [0,1,0,-1]

for h in range(H): # 어디에 익은 토마토, 그냥 토마토, 없는 칸인지 입력 받음
    for n in range(N):
        info = list(map(int,input().split()))
        box[h][n] = info
        for m in range(M):
            if info[m] == 1:
                red_tomato.append((m,n,h))
                result[h][n][m] = 0
            elif info[m] == -1:
                result[h][n][m] = -1
            else:
                check_zero = True

if check_zero == False:
    print(0)
else:
    queue = deque([])
    for i in red_tomato:
        queue.append(i)
    
    while queue:
        x,y,z = queue.popleft()
        for i in range(4):
            nextX = x + moveX[i]
            nextY = y + moveY[i]
            if 0 <= nextX < M and 0 <= nextY < N and result[z][nextY][nextX] == -2:
                result[z][nextY][nextX] = result[z][y][x] + 1
                queue.append((nextX,nextY,z))
        if 0 <= z-1 and result[z-1][y][x] == -2:
            result[z-1][y][x] = result[z][y][x] + 1
            queue.append((x,y,z-1))
        if z+1 < H and result[z+1][y][x] == -2:
            result[z+1][y][x] = result[z][y][x] + 1
            queue.append((x,y,z+1))

    print(check(M,N,H))