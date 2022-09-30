#합이 값은 부분집합
import sys


def dfs(l, sum):

    if sum>total//2:
        return #전체 합을 넘어갈 경우 불필요한 계산 없이 종료

    if l == n:
        if sum == (total-sum):
            print('YES')
            sys.exit(0) #프로그램 완전 종료
    else:
        dfs(l+1, sum+a[l])
        dfs(l+1, sum)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    dfs(0, 0)
    print('NO')