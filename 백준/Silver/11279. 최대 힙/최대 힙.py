import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def push(x):
    if len(heap) == 0:
        heap.append(x)
        return
    index = len(heap)
    heap.append(x)
    while index > 0:
        next_index = (index - 1) // 2
        if heap[index] > heap[next_index]:
            heap[index], heap[next_index] = heap[next_index], heap[index]
            index = next_index
        else:
            break

def pop():
    if len(heap) == 0: return 0
    if len(heap) == 1: return heap.popleft()
    result = heap[0]
    heap[0] = heap.pop()
    index = 0
    while index*2 + 1 < len(heap):
        left = index*2 + 1
        right = index*2 + 2
        biggest = left
        if right < len(heap) and heap[biggest] < heap[right]:
            biggest = right
        if heap[index] < heap[biggest]:
            heap[index], heap[biggest] = heap[biggest], heap[index]
            index = biggest
        else:
            break
    return result

heap = deque([])
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        print(pop())
    else:
        push(x)