#나의 풀이
# a = [x for x in range(1, 21)]
# for i in range(10):
#     p, q = map(int, input().split())
#     b = a[p-1:q]
#     a = a[:p-1] + b[::-1] + a[q:]
#     print(a)
#강사님 풀이
'''
파이썬의 swap
a, b = b, a
'''
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')