import sys
input = sys.stdin.readline

N, R = map(int, input().split())
result = 0

z = R // N
if R % N == 0: z -= 1

if N == 1: result = N * R * 2
elif R == 1: result = N + 1
elif N >= R: result = N + R-1 + R
else:
    R = R - z*N
    result = N + R-1 + R + z*N*2

print(result)