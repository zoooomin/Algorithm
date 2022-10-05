import itertools as it
n, f = map(int, input().split())
b = [1] * n
cnt = 0
for i in range(1, n):
    b[i] = b[i-1] * (n-i) / i #이항 계수 초기화
a = list(range(1, n+1)) #1부터 n까지 초기화
#모든 순열 경우의 수를 구해주는 it.permutations
for tmp in it.permutations(a):
    sum = 0
    for l, x in enumerate(tmp):
        sum += (x*(b[l]))
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break