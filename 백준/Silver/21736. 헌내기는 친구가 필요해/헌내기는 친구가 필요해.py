import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
campus = [[True for _ in range(M)] for i in range(N)]
people = [[False for _ in range(M)] for i in range(N)]
moveX = [-1,0,1,0]
moveY = [0,1,0,-1]
x = 0
y = 0
count = 0

for col in range(N):
    info = input()
    for row in range(M):
        if info[row] == 'P':
            people[col][row] = True
        elif info[row] == 'I':
            x = row
            y = col
        elif info[row] == 'X':
            campus[col][row] = False

queue = deque([(x,y)])
campus[y][x] = False
while queue:
    X, Y = queue.popleft()
    for i in range(4):
        nextX = X + moveX[i]
        nextY = Y + moveY[i]
        if 0 <= nextX < M and 0 <= nextY < N:
            if campus[nextY][nextX]:
                queue.append((nextX, nextY))
                campus[nextY][nextX] = False
                if people[nextY][nextX]: count += 1

if count == 0:
    print("TT")
else:
    print(count)