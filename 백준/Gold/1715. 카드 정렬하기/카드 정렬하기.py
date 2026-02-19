import sys
input = sys.stdin.readline

n = int(input())

if n <= 1:
    if n == 1:
        input()
    print(0)
    sys.exit()

card = []

def push(num):
    index = len(card)
    card.append(num)
    while index > 0:
        parent = (index - 1) // 2
        if card[index] < card[parent]:
            card[index], card[parent] = card[parent], card[index]
            index = parent
        else:
            break

def delete():
    if len(card) == 1:
        return card.pop()

    root = card[0]
    card[0] = card.pop()

    index = 0

    while True:
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index

        if left < len(card) and card[left] < card[smallest]:
            smallest = left
        if right < len(card) and card[right] < card[smallest]:
            smallest = right

        if smallest != index:
            card[index], card[smallest] = card[smallest], card[index]
            index = smallest
        else:
            break
    return root

for _ in range(n):
    push(int(input()))

result = 0
while len(card) > 1:
    a = delete()
    b = delete()
    combined = a + b
    result += combined
    push(combined)

print(result)