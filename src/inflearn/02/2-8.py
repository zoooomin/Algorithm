#뒤집은 소수(나의 풀이)
# n = int(input())
# x = list(map(int, input().split()))
#
#
# def reverse(a):
#     cnt = len(str(a)) - 1
#     new_num = 0
#     while a > 0:
#         t = a % 10
#         a = a//10
#         new_num = new_num + t * (10 ** cnt)
#         cnt -= 1
#     return new_num
#
# def isPrime(res):
#     chk = 0
#     for i in range(2, res):
#         if res % i ==0:
#             chk = 1
#             break
#     if chk == 0:
#         print(res,end=' ')
#
# for a in x:
#     res = reverse(a)
#     isPrime(res)
#강사님 풀이
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
        #123
        '''
        res = 3
        res = 30 + 2
        res = 320 + 1
        '''
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

n=int(input())
a=list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp,end=' ')