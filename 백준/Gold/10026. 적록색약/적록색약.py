import sys
from collections import deque
input = sys.stdin.readline

moveX = [-1,0,1,0]
moveY = [0,1,0,-1]

def BFS(x,y,color):
    queue = deque([])
    queue.append((x,y))
    visited[y][x] = True

    while queue:
        X,Y = queue.popleft()
        for i in range(4):
            nextX = X + moveX[i]
            nextY = Y + moveY[i]
            if 0 <= nextX < N and 0 <= nextY < N and graph[nextY][nextX] == color and visited[nextY][nextX] == False:
                queue.append((nextX, nextY))
                visited[nextY][nextX] = True

def BFS2(x,y,color):
    queue = deque([])
    queue.append((x,y))
    visited[y][x] = True

    while queue:
        X,Y = queue.popleft()
        for i in range(4):
            nextX = X + moveX[i]
            nextY = Y + moveY[i]
            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == False:
                if (color == 'R' or color == 'G') and (graph[nextY][nextX] == 'R' or graph[nextY][nextX] == 'G'):
                    queue.append((nextX, nextY))
                    visited[nextY][nextX] = True
                elif graph[nextY][nextX] == color:
                    queue.append((nextX, nextY))
                    visited[nextY][nextX] = True

result1 = 0
result2 = 0
N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]
graph = []

for _ in range(N):
    info = list(input())
    graph.append(info)

for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            BFS(x,y,graph[y][x])
            result1 += 1

visited = [[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            BFS2(x,y,graph[y][x])
            result2 += 1

print(result1, result2)