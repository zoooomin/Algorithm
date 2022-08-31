def find_even_number(n, m):
    numbers = [i for i in range(n, m+1)]
    median = find_med(numbers)#numbers에서 중앙값을 구하는 함수

    for i in numbers:
        if i % 2 == 0:
            print(i ,'짝수')
            if i == median:
                print(i ,'중앙값')

def find_med(numbers):
    if len(numbers) % 2 == 0:#자료의 수가 짝수인 경우 : (자료의 수/2번째 + 자료의수/2+1번째)/2 // 하지만 리스트는 0번부터 시작하므로 1을 빼주어야함!!
        median = numbers[int(len(numbers)/2-1)], numbers[int(len(numbers)/2)]
        median = sum(median)/2

    else:#자료의 수가 홀수인 경우 : 자료의 수/2+1번째
        median = numbers[int(len(numbers)/2)]

    return median
n = int(input('첫 번째 수 입력: '))
m = int(input('두 번째 수 입력: '))
find_even_number(n,m)