import sys
input = sys.stdin.readline

def pop():
    if len(arr) == 0: return 0
    if len(arr) == 1: return arr.pop()

    result = arr[0]
    arr[0] = arr.pop()
    idx = 0

    while (idx * 2) + 1 < len(arr):
        smallest = idx
        left = idx*2 + 1
        right = idx*2 + 2

        if arr[smallest] > arr[left]: smallest = left
        if right < len(arr) and arr[smallest] > arr[right]: smallest = right

        if smallest == idx: break
        arr[smallest], arr[idx] = arr[idx], arr[smallest]

        idx = smallest

    return result

def push(num):
    idx = len(arr)
    arr.append(num)

    while (idx - 1) // 2 >= 0:
        parent = (idx - 1) // 2

        if arr[parent] > arr[idx]:
            arr[parent], arr[idx] = arr[idx], arr[parent]
            idx = parent
        else: break

N = int(input())
arr = []

for _ in range(N):
    cmd = int(input())

    if cmd == 0: print(pop())
    else: push(cmd)