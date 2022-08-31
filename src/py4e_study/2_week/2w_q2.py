# Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅시다.
def yearly_payment(monthly_payment):
    # btax_payment : 세전 연봉
    # atax_payment : 세후 연봉
    btax_payment = 12 * monthly_payment  # 만원 단위
    if btax_payment <= 1200:
        atax_payment = btax_payment * (1 - 0.06)
    elif btax_payment <= 4600:
        atax_payment = btax_payment * (1 - 0.15)
    elif btax_payment <= 8800:
        atax_payment = btax_payment * (1 - 0.24)
    elif btax_payment <= 15000:
        atax_payment = btax_payment * (1 - 0.35)
    elif btax_payment <= 30000:
        atax_payment = btax_payment * (1 - 0.38)
    elif btax_payment <= 50000:
        atax_payment = btax_payment * (1 - 0.40)
    else:
        atax_payment = btax_payment * (1 - 0.42)

    print('세전 연봉: %i만원' % btax_payment)
    print('세후 연봉: %i만원' % atax_payment)


monthly_payment = int(input('월급을 입력하세요: '))
yearly_payment(monthly_payment)