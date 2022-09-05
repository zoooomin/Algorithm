#격자판 회문수
# a = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
# for i in range(7):
#     for j in range(3):
#         p = list()
#         q = list()
#         for t in range(5):
#             p.append(a[i][j+t])
#             q.append(a[j+t][i])
#         if p == p[::-1]:
#             print(p)
#             cnt += 1
#         if q == q[::-1]:
#             print(q)
#             cnt += 1
# print(cnt)
#강사님 풀이
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if a[i+k][j] != a[i+4-k][j]:
                break
        else:
            cnt += 1