import sys
input = sys.stdin.readline

words = list(map(str, input().split()))
result = []

for word in words:
    n = len(word)
    word = word.lower()

    if n == 1: result.append(word[0].upper())
    elif n % 2 != 0:
        if (n//2) % 2 == 0: result.append(word[len(word)//2].upper())
        else: result.append(word[len(word)//2].lower())
    else:
        idx2 = n//2
        idx1 = idx2 - 1

        if word[idx1] < word[idx2]: # idx1 부분이 사전순 앞쪽
            if idx1 % 2 == 0: result.append(word[idx1].upper())
            else: result.append(word[idx1].lower())
        elif word[idx1] > word[idx2]:
            if idx2 % 2 == 0: result.append(word[idx2].upper())
            else: result.append(word[idx2].lower())
        else: result.append(word[idx2].upper())

for s in result:
    print(s, end='')

# 단어 길이 홀수 -> word[len(word)//2]
# 단어 길이 짝수
    # len(word)//2 와 len(word)//2 - 1 비교
    # idx1 -> 짝수, idx2 -> 홀수