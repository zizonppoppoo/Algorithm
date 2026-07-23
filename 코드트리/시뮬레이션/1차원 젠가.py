# 문제 : https://www.codetree.ai/ko/trails/complete/curated-cards/intro-jenga-1d/description
n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

next_blocks = []
for i in range(s1-1):
    next_blocks.append(blocks[i])
for i in range(e1,n,1):
    next_blocks.append(blocks[i])

result = []
for i in range(s2-1):
    result.append(next_blocks[i])
for i in range(e2,len(next_blocks),1):
    result.append(next_blocks[i])

if len(result) == 0:
    print(0)
else:
    print(len(result))
    for n in result: print(n)