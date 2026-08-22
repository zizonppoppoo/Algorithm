import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
minus = zero = one = 0

def check(x1, y1, x2, y2):
    num = papers[y1][x1]

    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if papers[y][x] != num: return False

    return True

queue = deque([])
queue.append((0, 0, N-1, N-1))

while queue:
    x1, y1, x2, y2 = queue.popleft()

    if check(x1, y1, x2, y2) == True:
        if papers[y1][x1] == -1: minus += 1
        elif papers[y1][x1] == 0: zero += 1
        elif papers[y1][x1] == 1: one += 1

    else:
        n = (x2 - x1 + 1) // 3
        for i in range(3):
            for j in range(3):
                queue.append((x1 + j*n, y1 + i*n, x1 + j*n + n - 1, y1 + i*n + n - 1))


print(minus)
print(zero)
print(one)