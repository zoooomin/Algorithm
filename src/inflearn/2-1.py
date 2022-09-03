cnt = 0
a, b = map(int, input().split())
for i in range(1, a+1):
    if a % i == 0:
        cnt += 1
    if b == cnt:
        print(i)
        break
else:
   print(-1)