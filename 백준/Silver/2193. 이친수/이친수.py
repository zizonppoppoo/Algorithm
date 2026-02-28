import sys
input = sys.stdin.readline

N = int(input())
ones = 1
zeros = 1

if N == 1:
    print(ones)
elif N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    for i in range(N-3):
        temp = ones
        ones = zeros
        zeros += temp
    print(ones+zeros)