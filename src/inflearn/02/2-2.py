T = int(input())
for i in range(T):
    n, s, e, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    nums_s = nums[s-1:e]
    nums_s.sort()
    print(nums_s[2])