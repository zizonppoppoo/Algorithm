import math
n, m = map(int, input().split())
arr = []
num_list = []

for i in range(int(math.sqrt(m)+1)): # 2부터 m까지 수를 arr에 넣음
    arr.append(i)
arr[1] = 0
result = 0

for i in range(2,int(math.sqrt(m)+1)): # 소수 판별
    if arr[i] == 0:
        continue
    for j in range(i+i, int(math.sqrt(m)+1), i):
        arr[j] = 0

for i in range(int(math.sqrt(m)+1)): # 소수인 수를 num_list에 넣음
    if arr[i] == 0:
        continue
    else:
        num_list.append(arr[i])

for i in num_list:
    check = i*i
    if check > m:
        break
    while check < m+1:
        if check >= n:
            result += 1
        check *= i

print(result)