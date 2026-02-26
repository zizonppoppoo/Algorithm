import sys
read = sys.stdin.readline
for _ in range(int(read())):
    x1, y1, x2,y2 = map(int,read().split())
    n = int(read())
    l = [list(map(int,read().split())) for i in range(n)]
    result = 0
    for c in l:
        if (x1-c[0])**2 + (y1-c[1])**2 < c[2]**2:
            if (x2-c[0])**2 + (y2-c[1])**2 < c[2]**2:
                pass
            else:
                result += 1
        elif (x2-c[0])**2+(y2-c[1])**2 < c[2]**2:
            result += 1
    print(result)