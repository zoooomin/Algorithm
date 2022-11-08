#네트워크 선 자르기
#재귀, 메모이제이션(top-down)
def dfs(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1 or n == 2:
        return n
    else:
        dy[n] = dfs(n-1) + dfs(n-2)
        return dy[n]

if __name__ == '__main__':
    n = int(input())
    dy =[0] * (n+1)
    print(dfs(n))