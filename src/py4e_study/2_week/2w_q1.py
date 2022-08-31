#Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
import random
#가위:0, 바위:1, 보:2
def game(you):
    computer = random.randint(0, 2)
    if (computer == 0):
        print('computer : 가위')
        if(you == 1):
            print('you : 바위')
            print('당신이 이겼습니다!')
        elif(you ==2):
            print('you : 보')
            print('컴퓨터가 이겼습니다.')
        else:
            print('you : 가위')
            print('비겼습니다.')

    elif (computer == 1):
        print('computer : 바위')
        if(you == 0):
            print('you : 가위')
            print('컴퓨터가 이겼습니다.')
        elif(you ==2):
            print('you : 보')
            print('당신이 이겼습니다!')
        else:
            print('you : 바위위')
            print('비겼습니다.')

    elif (computer == 2):
        print('computer : 보')
        if(you == 0):
            print('you : 가위')
            print('당신이 이겼습니다!')
        elif(you ==1):
            print('you : 바위')
            print('컴퓨터가 이겼습니다.')
        else:
            print('you : 보')
            print('비겼습니다.')

you = int(input('가위:0, 바위:1, 보:2 입니다. 원하는 선택지를 입력해주세요: '))
game(you)
