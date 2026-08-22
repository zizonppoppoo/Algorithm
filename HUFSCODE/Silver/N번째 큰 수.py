import sys
input = sys.stdin.readline

def push(num):
    idx = len(heap)
    heap.append(num)

    while idx > 0:
        parent = (idx - 1) // 2

        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else: break

def pop_min():
    if len(heap) == 1: return heap.pop()

    result = heap[0]
    heap[0] = heap.pop()
    idx = 0

    while idx*2 + 1 < len(heap):
        smallest = idx

        if heap[idx] > heap[idx*2 + 1]:
            smallest = idx*2 + 1
        if idx*2 + 2 < len(heap) and heap[smallest] > heap[idx*2 + 2]:
            smallest = idx*2 + 2

        if smallest == idx: break
        else:
            heap[smallest], heap[idx] = heap[idx], heap[smallest]
            idx = smallest

    return result

    

N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))

    for num in nums:
        if len(heap) < N: push(num)
        elif heap[0] < num:
            pop_min()
            push(num)

print(pop_min())