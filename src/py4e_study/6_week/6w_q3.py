'다시한번 보기'
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
def stock_profit(stocks, sells):
    stocks_s = stocks.split(',')
    li = list()
    di = dict()
    i = 0
    for st in stocks_s:
        li.append(st.split(('/'))) #모두 str

    for s in li:
        rate = (sells[i] - int(s[2]))/int(s[2]) * 100
        i += 1
        tup = (s[0], rate)
        di[rate] = s[0]
    di = dict((sorted(di.items(), reverse=True)))
    for k, v in di.items():
        print(f'{v}의 수익률 {k:.3}')

stock_profit(stocks, sells)
