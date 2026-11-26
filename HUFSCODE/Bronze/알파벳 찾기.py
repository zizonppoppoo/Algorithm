import sys
input = sys.stdin.readline

word = input().strip()
result = [-1] * 26

for i in range(len(word)):
    alphabet = word[i]

    if result[ord(alphabet) - ord('a')] == -1:
        result[ord(alphabet) - ord('a')] = i

for n in result:
    print(n, end = ' ')