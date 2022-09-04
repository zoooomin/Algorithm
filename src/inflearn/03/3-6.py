# 나의 풀이
#n = int(input())
# a = list()
#
# for i in range(n):
#     x = list(map(int, input().split()))
#     a.append(x)
# p, q, r, s = 0, 0, 0, 0
# max = 0
# for i in range(n):
#     p = p + a[i][i]
#     q = q + a[n - i - 1][i]
#     if p < q:
#         max = q
#     else:
#         max = p
#     for j in range(n):
#         r = r + a[i][j]
#         s = s + a[j][i]
#     if r > max:
#         max = r
#     elif s > max:
#         max = s
#     r = 0
#     s = 0
# print(max)

#강사님 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -214700000
#행과 열의 합
for i in range(n):
    #행의 합 sum1,열의 합 sum2
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[n-i-1][i]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)