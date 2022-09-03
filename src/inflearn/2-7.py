#내가 푼 풀이
# n = int(input())
# cnt = 0
# for i in range(2, n+1):
#     chk = 1
#     for j in range(2, i):
#         if i % j == 0:
#             chk = 0
#             break
#     if chk == 1:
#         cnt += 1
# print(cnt)
#강사님의 풀이//20만을 입력값으로 넣었을 때 확실히 빠르다..
#에라토스테네스 체
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
