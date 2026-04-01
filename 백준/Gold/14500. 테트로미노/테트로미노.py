import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

result = 0

for col in range(N - 1):
    for row in range(M - 1):
        tmp = paper[col][row] + paper[col+1][row] + paper[col][row+1] + paper[col+1][row+1]
        if tmp > result: result = tmp

for col in range(N - 3):
    for row in range(M):
        tmp = paper[col][row] + paper[col+1][row] + paper[col+2][row] + paper[col+3][row]
        if tmp > result: result = tmp

for col in range(N):
    for row in range(M - 3):
        tmp = paper[col][row] + paper[col][row+1] + paper[col][row+2] + paper[col][row+3]
        if tmp > result: result = tmp

for col in range(N - 1):
    for row in range(M - 2):
        shapes = [
            paper[col][row] + paper[col+1][row] + paper[col+1][row+1] + paper[col+1][row+2],
            paper[col][row+2] + paper[col+1][row] + paper[col+1][row+1] + paper[col+1][row+2],
            paper[col][row] + paper[col][row+1] + paper[col][row+2] + paper[col+1][row],
            paper[col][row] + paper[col][row+1] + paper[col][row+2] + paper[col+1][row+2],
            paper[col][row+1] + paper[col+1][row] + paper[col+1][row+1] + paper[col+1][row+2],
            paper[col][row] + paper[col][row+1] + paper[col][row+2] + paper[col+1][row+1],
            paper[col][row+1] + paper[col][row+2] + paper[col+1][row] + paper[col+1][row+1],
            paper[col][row] + paper[col][row+1] + paper[col+1][row+1] + paper[col+1][row+2]
        ]
        max_val = max(shapes)
        if max_val > result: result = max_val

for col in range(N - 2):
    for row in range(M - 1):
        shapes = [
            paper[col][row] + paper[col+1][row] + paper[col+2][row] + paper[col+2][row+1],
            paper[col][row] + paper[col+1][row] + paper[col+2][row] + paper[col][row+1],
            paper[col][row+1] + paper[col+1][row+1] + paper[col+2][row+1] + paper[col][row],
            paper[col][row+1] + paper[col+1][row+1] + paper[col+2][row+1] + paper[col+2][row],
            paper[col][row] + paper[col+1][row] + paper[col+2][row] + paper[col+1][row+1],
            paper[col][row+1] + paper[col+1][row+1] + paper[col+2][row+1] + paper[col+1][row],
            paper[col][row] + paper[col+1][row] + paper[col+1][row+1] + paper[col+2][row+1],
            paper[col][row+1] + paper[col+1][row+1] + paper[col+1][row] + paper[col+2][row]
        ]
        max_val = max(shapes)
        if max_val > result: result = max_val

print(result)