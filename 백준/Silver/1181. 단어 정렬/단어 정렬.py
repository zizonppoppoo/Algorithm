import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    word = input()
    arr.add(word)

result = sorted(arr, key = lambda x : (len(x),x))
for word in result:
    print(word, end='')