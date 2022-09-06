def Count(mid):
    cnt = 1
    ep = l[0]
    for i in range(1, n):
        if l[i] - ep >= mid:
            cnt += 1
            ep = l[i]

    return cnt

n, c = map(int, input().split())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)
l.sort()
lt = 1
rt = l[-1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
'''
가장 가까운 말의 거리
즁앙값
'''