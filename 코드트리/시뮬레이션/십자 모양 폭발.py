# 문제 : https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-bomb/description

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split()) # 폭탄위치 - r:행, c:열

result = [[0 for _ in range(n)] for _ in range(n)]
level = grid[r-1][c-1]
grid[r-1][c-1] = 0

for i in range(1,level):
    if c-1-i >= 0: grid[r-1][c-1-i] = 0
    if c-1+i < n: grid[r-1][c-1+i] = 0
    if r-1-i >= 0: grid[r-1-i][c-1] = 0
    if r-1+i < n: grid[r-1+i][c-1] = 0

for col in range(n):
    index = n-1
    for row in range(n-1,-1,-1):
        if grid[row][col] != 0:
            result[index][col] = grid[row][col]
            index -= 1

for row in range(n):
    for col in range(n):
        print(result[row][col], end = ' ')
    print()