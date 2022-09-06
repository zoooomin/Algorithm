#뮤직비디오(결정알고리즘)
def function(mid):
    cnt = 1
    s = 0
    for x in a:
        if s + x <= mid:
            s += x
        else:
            cnt += 1
            s = x
    return cnt

n, m = map(int, input().split())

a = list(map(int, input().split()))
a. sort()
lt = a[-1]
rt = sum(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if function(mid) <= m:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1

print(res)

