from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [ [] for i in range(n+1) ]
distance = [ -1 for i in range(n+1) ]

def BFS(x):
    queue = deque([])
    distance[x] = 0
    queue.append(x)
    while len(queue) > 0:
        node = queue.popleft()
        for j in graph[node]:
            if distance[j] == -1:
                distance[j] = distance[node] + 1
                queue.append(j)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
BFS(x)
result = []

for i in range(1,n+1):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)