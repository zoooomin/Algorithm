import random

rand_num = []
for i in range(3):
    number = random.randint(0, 100)
    if number not in rand_num:
        rand_num.append(number)

rand_num.sort()
min = rand_num[0]
mid = rand_num[1]
max = rand_num[2]

s = 1
cnt = 0
my_num_list = []

while True:
    print(f'{s}차 시도')
    my_num = int(input('숫자를 예측해보세요: '))

    if my_num in my_num_list:
        print('이미 예측에 사용한 숫자입니다.')
        s -= 1
    else:
        my_num_list.append(my_num)

    if my_num in rand_num:
        print('숫자를 맞추셨습니다!',end=" ")
        if my_num == min:
            print(f'{my_num}는 최솟값입니다.')
            cnt += 1
        elif my_num == mid:
            print(f'{my_num}는 중간값입니다.')
            cnt += 1
        elif my_num == max:
            print(f'{my_num}는 최댓값입니다.')
            cnt += 1
    else:
        print(f'{my_num}는 없습니다.')
        if s >=5 and s < 10:
            if my_num < min:
                print(f'{my_num}는 최솟값보다 작습니다.')
            elif my_num > min:
                print(f'{my_num}는 최솟값보다 큽니다.')
        elif s >= 10:
            if my_num < max:
                print(f'{my_num}는 최댓값보다 작습니다.')
            elif my_num > max:
                print(f'{my_num}는 최댓값보다 큽니다.')
    if cnt == 3:
        print('gameover')
        print(f'{s}번 시도만에 예측 성공')
        break
    s += 1