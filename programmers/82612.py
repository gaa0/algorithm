def solution(price, money, count):
    sum_price = 0
    for i in range(1, count + 1):
        sum_price += i * price
    result = money - sum_price
    answer = 0
    if result < 0:
        answer = -result
    return answer

price = 3
money = 20
count = 4
print(solution(price, money, count))
