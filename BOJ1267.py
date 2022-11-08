n = int(input())
call_time = list(map(int, input().split()))

y_total = 0
m_total = 0

for i in call_time:
    y_price = 0
    m_price = 0
    y_quotient = i // 30
    m_quotient = i // 60

    y_price += y_quotient * 10
    m_price += m_quotient * 15


    y_remain = i % 30
    m_remain = i % 60


    if y_remain >= 0 and y_remain <= 29:
        y_price += 10
    if m_remain >= 0 and m_remain <= 59:
        m_price += 15

    y_total += y_price
    m_total += m_price

if y_total < m_total:
    print("Y {}".format(y_total))
elif m_total < y_total:
    print("M {}".format(m_total))
elif m_total == y_total:
    print("Y M {}".format(y_total))