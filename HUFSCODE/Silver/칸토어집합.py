import sys
input = sys.stdin.readline

nums = list(map(int, sys.stdin.read().split()))
result = ['-']

for n in nums:
    if n < len(result): print(result[n])
    else:
        while n >= len(result):
            result.append(result[-1] + ' ' * len(result[-1]) + result[-1])
        print(result[-1])