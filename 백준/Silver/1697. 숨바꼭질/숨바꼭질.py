import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
result = [-1] * 100001

def BFS(n,k):
    if n == k: return 0
    queue = deque([])
    queue.append(n)
    while True:
        node = queue.popleft()
        if node - 1 >= 0 and node - 1 <= 100000 and result[node - 1] == -1:
            result[node - 1] = result[node] + 1
            if node - 1 == k:
                return result[node - 1]
            else:
                queue.append(node - 1)
        if node + 1 <= 100000 and result[node + 1] == -1:
            result[node + 1] = result[node] + 1
            if node + 1 == k:
                return result[node + 1]
            else:
                queue.append(node + 1)
        if node * 2 <= 100000 and result[node*2] == -1:
            result[node*2] = result[node] + 1
            if node*2 == k:
                return result[node * 2]
            else:
                queue.append(node * 2)
result[n] = 0
print(BFS(n,k))