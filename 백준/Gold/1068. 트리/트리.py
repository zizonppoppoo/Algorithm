import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
visited = [(False)] * (n+1)

def BFS(root):
    result = 0
    visited[root] = True
    queue = deque([])
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        check = True
        for i in tree[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                check = False
        if check: result += 1
    return result

numbers = list(map(int, input().split()))
for i in range(n):
    x = numbers[i]
    if x == -1:
        root = i
    else:
        tree[i].append(x)
        tree[x].append(i)

k = int(input())
if k == root:
    print(0)
else:
    visited[k] = True
    print(BFS(root))