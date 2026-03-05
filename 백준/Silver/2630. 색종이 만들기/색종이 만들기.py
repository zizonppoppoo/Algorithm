N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white_count = 0
blue_count = 0

def cut(matrix, r, c, size):
    global white_count
    global blue_count
    count = 0

    for col in range(c, c+size):
        for row in range(r, r+size):
            count += matrix[col][row]
    if count == 0:
        white_count += 1
        return
    elif count == size*size:
        blue_count += 1
        return
    nextsize = size//2
    cut(matrix, r, c, nextsize)
    cut(matrix, r+nextsize, c, nextsize)
    cut(matrix, r, c+nextsize, nextsize)
    cut(matrix, r+nextsize, c+nextsize, nextsize)

cut(matrix, 0, 0, N)
print(white_count)
print(blue_count)