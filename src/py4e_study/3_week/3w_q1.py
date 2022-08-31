def gugudan(number):
    i = 1
    print(f'{number}단')

    while True:
        result = number * i
        if result > 50:#값이 50을 초과한다면 반복분 탈출
            break

        print(f'{number} X {i} = {result}')
        i = i + 2 #홀 수 번째를 출력하기 위한 i값

number = int(input('몇 단?: '))
gugudan(number)