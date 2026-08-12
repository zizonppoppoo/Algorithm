import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

words = set(words)
words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words: print(word)