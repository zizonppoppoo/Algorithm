import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

cnt = {}

for w in words:
    if len(w) >= M:
        cnt[w] = cnt.get(w, 0) + 1
result = list(cnt.items())
result.sort()
result.sort(key=lambda x: len(x[0]), reverse = True)
result.sort(key=lambda x: x[1], reverse = True)

for i in range(len(result)):
    print(result[i][0])