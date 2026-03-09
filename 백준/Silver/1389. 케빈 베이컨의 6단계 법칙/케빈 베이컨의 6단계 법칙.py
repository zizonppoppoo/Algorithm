import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):
    visited[x] = False
    queue = deque([])
    queue.append(x)

    while queue:
        node = queue.popleft()
        for next in friends[node]:
            if visited[next]:
                queue.append(next)
                visited[next] = False
                count[next] = count[node] + 1
    counting = 0
    for num in count:
        counting += num
    return counting


N, M = map(int,input().split())
friends = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    friends[A].append(B)
    friends[B].append(A)

count = [0] * (N+1)
visited = [True] * (N+1)
least = BFS(1)
Result = 1

for i in range(2,N+1):
    count = [0] * (N+1)
    visited = [True] * (N+1)
    if BFS(i) < least:
        least = BFS(i)
        Result = i
print(Result)