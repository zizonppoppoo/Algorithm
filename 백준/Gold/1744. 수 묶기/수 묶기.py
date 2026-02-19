n = int(input())
minus = []
plus = []
zeros = 0
result = 0

for i in range(n):
    x = int(input())

    if x < 0:
        minus.append(x)
    elif x == 0:
        zeros += 1
    elif x == 1:
        result += 1
    else:
        plus.append(x)

minus.sort(reverse=True)
plus.sort()

while len(minus) > 1:
    result += minus.pop() * minus.pop()
if len(minus) == 1:
    if zeros == 0:
        result += minus.pop()
while len(plus) > 1:
    result += plus.pop() * plus.pop()
if len(plus) == 1:
    result += plus.pop()
print(result)