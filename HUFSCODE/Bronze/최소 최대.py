import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def quick_sort(start, end):
    if start >= end: return

    l = start
    r = end
    pivot = nums[(l+r) // 2]

    while l <= r:
        while nums[l] < pivot: l += 1
        while nums[r] > pivot: r -= 1

        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    quick_sort(start, r)
    quick_sort(l, end)

if n == 1: print(nums[0])
else:
    quick_sort(0,n-1)
    print(nums[0], nums[-1])