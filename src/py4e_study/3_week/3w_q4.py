def count_prime_number(n, m):
    sosu_count = 0
    for i in range(n, m+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt = cnt + 1 #약수 중에서 나누어 떨어지는 개수
        if cnt == 2: #1과 자기자신으로만 나누어 떨어질 경우 소수
            sosu_count = sosu_count + 1 #범위 중 소수 개수 카운트

    return sosu_count

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

sosu_count = count_prime_number(n, m)
print('소수 개수: ', sosu_count)