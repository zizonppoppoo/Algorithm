import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):
    queue = deque([])
    queue.append(x)

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if visited[next] == False:
                queue.append(next)
                visited[next] = True
                result[x][next-1] = 1

N = int(input())
graph = [[] for _ in range(N+1)]
result = [[0]*N for _ in range(N+1)]

for i in range(1,N+1):
    info = list(map(int,input().split()))
    for j in range(N):
        if info[j] == 1:
            graph[i].append(j+1)

for i in range(1,N+1):
    visited = [False] * (N+1)
    BFS(i)

for i in range(1,N+1):
    for num in result[i]:
        print(num,end=' ')
    print('')