# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     for j in range(n-1):
#         if a[i][j] > a[i][j+1]:
#             a[i][j+1] = 0
#         elif a[i][j] < a[i][j+1]:
#             a[i][j] = 0
# for i in range(n):
#     for j in range(n-1):
#         if a[j][i] > a[j+1][i]:
#             a[j+1][i] = 0
#         elif a[j][i] < a[j+1][j]:
#             a[j][i] = 0
#
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] != 0:
#             cnt += 1
# print(cnt)

#강사님 풀이
dx = [-1, 0, 1, 0] #i에 더하는 것
dy = [0, 1, 0, -1] #j에 더하는 것
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#가장자리를 0으로 초기화
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
