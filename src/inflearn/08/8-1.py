#네트워크 선 자르기
#동적계획법
#f(n) = f(n-1) + f(n-2)
n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]
print(dy[n])