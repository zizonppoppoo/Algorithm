import sys
input = sys.stdin.readline

def back(dp_idx, num):
     while dp_idx > 0:
          

N = int(input())
nums = list(map(int, input().split()))
dp = [[] for _ in range(N+1)]
dp[0].append((0,10000))

for dp_idx in range(1,N+1):

    for i in range(len(dp[dp_idx-1])):
            
            num_idx = N - dp_idx
            last_count, last_min = dp[dp_idx-1][i]

            if last_min > nums[num_idx]:
                dp[dp_idx].append((last_count + 1, nums[num_idx]))

            elif last_min == nums[num_idx]:
                dp[dp_idx].append((last_count, last_min))

            elif last_count == 1 and last_min < nums[num_idx]:
                dp[dp_idx].append((1, nums[num_idx]))

            else:
                