import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

len1 = len(word1)
len2 = len(word2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(len1):
    for j in range(len2):

        if word1[i] == word2[j]: dp[i+1][j+1] = dp[i][j] + 1
        else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len1][len2])