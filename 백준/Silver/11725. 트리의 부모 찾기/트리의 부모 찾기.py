import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
visited = [(False)] * (n+1)
result = [0 for i in range(n+1)]

def DFS(x):
    for i in tree[x]:
        if result[i] == 0:
            result[i] = x
            DFS(i)

for i in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

result[1] = 1
DFS(1)
for i in range(2,n+1):
    print(result[i])