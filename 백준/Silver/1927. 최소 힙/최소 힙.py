import sys
input = sys.stdin.readline

def push(x):
    index = len(heap)
    heap.append(x)
    if index == 0: return
    while index > 0:
        parent_index = (index-1)//2
        if heap[index] < heap[parent_index]:
            temp = heap[index]
            heap[index] = heap[parent_index]
            heap[parent_index] = temp
            index = parent_index
        else:
            return

def pop():
    if len(heap) == 0:
        return 0
    if len(heap) == 1:
        return heap.pop()

    result = heap[0]
    heap[0] = heap.pop()
    index = 0
    while index*2+1 < len(heap):
        left = index*2 + 1
        right = index*2 + 2
        smallest = left

        if right < len(heap) and heap[smallest] > heap[right]:
            smallest = right
        if heap[index] > heap[smallest]:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break
    return result

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(pop())
    else:
        push(x)