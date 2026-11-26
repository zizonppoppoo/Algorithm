import sys
input = sys.stdin.readline

H, W = map(int, input().split())
info = list((input().split('\n')) for _ in range(H))

result = [[-1]*W for _ in range(H)]

for y in range(H):
    check = False
    number = 0
    for x in range(W):
        boo = info[y][0][x]

        if boo == 'B':
            check = True
            number = 0

        if check == True:
            result[y][x] = number
            number += 1

for y in range(H):
    for x in range(W):
        print(result[y][x], end=' ')
    print()

        

# 세로 -> H, 가로 -> W
# 배달원은 동쪽으로만 이동