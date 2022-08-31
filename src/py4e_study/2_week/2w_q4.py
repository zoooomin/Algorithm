#Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.
def bus_fare(age, pay_with):
    #age:나이, pay_with:지불유형, pay:버스 요금
    if (age < 8 or age >= 75): #8세 미만이거나 75세 이상인 경우 지불유형과 상관없이 무료
        pay = '무료'
    else:
        if (pay_with == '카드'): #카드는 나이에 따라 450원/720원/1200원
            if age < 14:
                pay = '450원'
            elif age < 20:
                pay = '720원'
            else:
                pay = '1200원'
        elif (pay_with == '현금'): #현금은 나이에 따라 450원/1000원/1300원
            if age < 14:
                pay = '450원'
            elif age < 20:
                pay = '1000원'
            else:
                pay = '1300원'

    print('나이: %i세'%age)
    print('지불유형: %s'%pay_with)
    print('버스요금: %s'%pay)

age = int(input('나이를 입력해주세요: '))
pay_with = input('결제 수단을 입력해주세요(현금, 카드): ')
bus_fare(age, pay_with)