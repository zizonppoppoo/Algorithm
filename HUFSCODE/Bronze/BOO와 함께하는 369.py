import sys
input = sys.stdin.readline

N = int(input())
result = 0

for num in range(1, N + 1):
    for c in str(num):
        if c in "369":
            result += 1

print(result)