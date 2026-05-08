# 연산자
# 산술 연산자
# + - * /(나누기, 무조건 실수형태로 출력) %(나머지) //(몫) **(거듭제곱)

# 70p 동전교환기
# 10000원짜리 지폐를 500원, 100원짜리 동전으로 교환
money = 10000
print(money // 500)
print(money // 100)

# 몫, 나머지 --> 구입 가능한 사탕의 수
price = 450
numCandy = money // price
change = money % price
print(numCandy)
print(change)
print()

# 대입 연산자 '='
# 복합 대입 연산자 += -= *= /= //= %=
a = 10
a += 10 # a = a + 10
print(a) # 20

a -= 5 # a = a - 5
print(a) # 15


# 비교 연산자
# > < >= <= ==(같다) !=(같지않다)
