#방법1(더 좋은 방법)
n = int(input())
for i in range(n):
    w = list(input().lower())
    for j in range(len(w)//2):
        if w[j] != w[-(j+1)]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))
# 방법2
# n = int(input())
# for i in range(n):
#     w = input().lower()
#     if w == w[::-1]:
#         print(f'#{i+1} YES')
#     else:
#         print(f'#{i+1} NO')