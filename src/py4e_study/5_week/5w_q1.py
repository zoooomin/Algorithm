import random

current_num = 0

def my_turn(current_num):

    my = input('\nmy turn - 숫자를 입력하세요: ')
    my = my.split()
    my_num = list(map(int, my)) #my_num 리스트는 모두 정수형

    wrong1 = len(my_num) not in [1, 2, 3] #입력한 숫자가 3자리, 2자리, 1자리가 아닐경우
    wrong2 = my_num[0] != current_num + 1 #현재 숫자의 다음 숫자부터 입력하지 않았을 경우
    wrong3 = check_seq(my_num) #숫자를 순차적으로 입력했는지 체크

    if wrong1 or wrong2 or wrong3:
        print('잘못 입력 하였습니다. 다시 입력해 주세요')
        my_turn(current_num)

    else: #save last num
        current_num = my_num[-1] #현재 숫자 저장하기
        print('현재 숫자: ', current_num)
        if current_num == 31:
            print('you lose!!!!')
        else:
            computer_turn(current_num) #컴퓨터 차례에 현재 숫자 전달

def computer_turn(current_num):

    computer_turn_num = random.randint(1, 3) #몇가지 숫자를 출력할지 random으로 지정

    start_num = current_num + 1 #컴퓨터의 시작숫자는 무조건 현재 숫자보다 1 큰 숫자
    computer_num = start_num

    print('컴퓨터: ',end = " ")
    for i in range(computer_turn_num):
        print(computer_num, end=" ")
        computer_num += 1
    print()
    current_num = computer_num - 1 #내 차례에 현재 숫자를 전달하기 위해서는 컴퓨터가 마지막 출력한 숫자에서 -1
    print('현재 숫자: ',current_num)

    if current_num == 31:
        print('computer lose!!!')
    else:
        my_turn(current_num)

def check_seq(my_num):
    '''숫자를 순차적으로 입력했는지 체크하기'''
    '''순차적으로 입력했을 경우에는 false, 아닐경우에 true'''
    if len(my_num) == 3:
        if (my_num[2] - my_num[1]) == (my_num[1] - my_num[0]) == 1:
            return False
        else:
            return True
    elif len(my_num) == 2:
        if (my_num[1] - my_num[0] == 1):
            return False
        else:
            return True
    elif len(my_num) == 1:
        return False

#게임 시작
def bs31():
    print('배스킨라빈스 써리원 게임')
    print('-----------------')
    global current_num
    my_turn(current_num)

bs31()

