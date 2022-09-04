#수들의 합(다시)
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# t = 0
# cnt = 0
# for i in range(n):
#     s = a[i]
#     if s == m:
#         cnt += 1
#     for j in range(i+1, n):
#         s += a[j]
#         if s == m:
#             cnt += 1
#             break
#         elif s < m:
#             continue
#         else:
#             break
# print(cnt)
#강사님 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)