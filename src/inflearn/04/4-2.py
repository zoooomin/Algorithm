#랜선 자르기(결정 알고리즘)
def function(mid):
    cnt = 0
    for i in l:
        cnt += i // mid

    return cnt

k, n = map(int, input().split())
l = []
for _ in range(k):
    a = int(input())
    l.append(a)

lt = 1
rt = max(l)

while lt <= rt:
    mid = (lt + rt) // 2
    if function(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
print(res)