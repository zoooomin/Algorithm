# 나의 풀이
# s = input()
# t = ''
# for i in s:
#     if (ord(i) > 47) and (ord(i) < 58):
#         t += i
#     t = t.lstrip('0')
#
# n = int(t)
# print(n)
#
# cnt = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         cnt += 1
# print(cnt)
#강사님 풀이
s = input()
res = 0
for i in s:
    if i.isdecimal():
        res = res * 10 + int(i)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)