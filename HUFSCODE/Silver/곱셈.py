import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
# A를 B번 곱한 수를 C로 나눈 나머지

num = A % C
result = A
for _ in range(B):
    result = (result * num) % C

print(result)