# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# m = int(input())
# b = [list(map(int, input().split())) for _ in range(m)]
# for i in range(m):
#     r = b[i][0] - 1 #행 자리
#     cnt = b[i][1] #왼쪽, 오른쪽
#     v = b[i][2] #회전수
#     if v > n:
#         v = n-v
#     if cnt == 0:
#         p = 0
#         q = p + v
#         a[r] = a[r][q:]+a[r][p:q]
#     elif cnt == 1:
#         p = n
#         q = n-v
#         a[r] = a[r][q:p] + a[r][:q]
#
# s =0
# e = n
# tot = 0
# for i in range(n):
#     for j in range(s, e):
#         tot += a[i][j]
#
#     if s != n//2:
#         s += 1
#         e -= 1
#     if s == n//2:
#         s -= 1
#         e += 1
# print(tot)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int,input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) #하나의 왼쪽회전이 이루어짐
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())#오른쪽 회전

s = 0
e = n
tot = 0
for i in range(n):
    for j in range(s, e):
        tot += a[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(tot)