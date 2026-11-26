import sys
from collections import deque
input = sys.stdin.readline

def check(x, y, R, C):
    checkList = [[False]*C for _ in range(R)]
    checkList[x][y] = True
    q = deque()
    q.append((x, y))
    
    while True:
        cx, cy = q.popleft()

        if chair[cx][cy] == False:
            chair[cx][cy] = True
            result.append((cx, cy))
            return

        else:
            for i in range(4):
                nx = x + move[i][0]
                ny = y + move[i][1]

                if 0 <= nx < R and 0 <= ny < C and checkList[nx][ny] == False:
                    q.append((nx, ny))
                    checkList[nx][ny] = True


R, C, N = map(int, input().split())
prefer = []
chair = [[False]*C for _ in range(R)]
result = []
move = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for _ in range(N):
    x, y = map(int, input().split())
    prefer.append((x, y))

for i in range(N):
    x, y = prefer[i]

    if chair[x][y] == False:
        chair[x][y] = True
        result.append((x, y))

    else: check(x, y, R, C)

for i in range(N):
    print(result[i][0], result[i][1])


# 선호좌석 이미 차있는 경우 우선순위
# 1. 위, 왼, 오, 아래