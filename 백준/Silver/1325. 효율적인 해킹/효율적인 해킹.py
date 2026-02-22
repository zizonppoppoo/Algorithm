import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def BFS(x):
    q = deque([x])
    visited = [False] * (n + 1)
    visited[x] = True
    count = 1

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1
    return count

max = 0
result = []

for i in range(1, n + 1):
    if not graph[i]:
        continue

    cnt = BFS(i)
    if cnt > max:
        max = cnt
        result = [i]
    elif cnt == max:
        result.append(i)

print(*(result if result else range(1, n+1)))