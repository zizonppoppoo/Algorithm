import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n : 응시자 수, k : 상 받는 사람 수
scores = list(map(int, input().split()))

def quick_sort(start, end):
    if start >= end: return

    l = start
    r = end
    pivot = scores[((l+r) // 2)]

    while l <= r:
        while scores[l] < pivot: l += 1
        while scores[r] > pivot: r -= 1

        if l <= r:
            scores[l], scores[r] = scores[r], scores[l]
            l += 1
            r -= 1

    quick_sort(start, r)
    quick_sort(l, end)

if n == 1: print(scores[0])
else:
    quick_sort(0, n-1)
    print(scores)
    for _ in range(k-1): scores.pop()
    print(scores.pop())