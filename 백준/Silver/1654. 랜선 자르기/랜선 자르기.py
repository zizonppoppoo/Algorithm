K, N = map(int, input().split())
lan = [0] * K
right = 0
left = 1
result = 0

for i in range(K):
    x = int(input())
    lan[i] = x
    if x > right:
        right = x

while right >= left:
    cm = (right+left) // 2
    count = 0
    for i in range(K):
        count += lan[i] // cm
    if count < N:
        right = cm - 1
    elif count >= N:
        if result < cm:
            result = cm
        left = cm + 1

print(result)