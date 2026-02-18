import sys

n, m = map(int, sys.stdin.readline().split())
cant_hear = set()
result = []

for i in range(n):
    name = input()
    cant_hear.add(name)

for i in range(m):
    name = input()
    if name in cant_hear:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)