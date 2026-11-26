import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

room = [[0 for _ in range(N)] for _ in range(N)]
move = [(0, 1), (-1, 0), (0, -1)]

x = N//2
y = N//2
room[y][x] = 1
result = [x, y]

number = 2
y -= 1

for i in range(N//2):

        for k in range(2*i + 1):
            room[y][x] = number
            if number == K:
                result[0] = x
                result[1] = y
            number += 1
            x += 1

        for k in range(3):
            for j in range((i+1)*2):
                if number == K:
                    result[0] = x
                    result[1] = y
                room[y][x] = number
                number += 1
                x += move[k][0]
                y += move[k][1]

        if number == K:
            result[0] = x
            result[1] = y
        room[y][x] = number
        number += 1

        y -= 1

for i in range(N):
    for n in room[i]:
        print(n, end=' ')
    print()

for n in result:
    print(n+1, end=' ')




'''
@ @ @ -> 2번씩
@ @ @ @ @ -> 4번씩
@ @ @ @ @ @ @ -> 6번씩

@ * @
@ * @
@ @ @

@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
'''