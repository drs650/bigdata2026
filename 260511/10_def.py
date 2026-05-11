# def coffee():
# 	print('오늘은 석쌤이 커피를 쏩니다.')
# 	result = '아메리카노'
# 	return result
	
# cup = coffee() # 함수 호출
# print(cup)

# def add_sub(n1, n2): # 함수 정의
#     return n1 + n2, n1 - n2

# x, y = add_sub(1, 2) # 함수 호출
# print(x, y)

# print(add_sub(200,100)) # 함수 호출

# 가변 매개변수 *args
# 함수 정의 -> 정수를 몇 개를 더해야 할지 정해지지 않았다.
# -> 가변 매개변수로 하겠다.
# def adder(*args): # 튜플로 묶겠다(튜플 패킹) --> *
#     total = sum(args) # sum() : 합계를 구하는 내장함수
#     return total

# # 함수 호출
# result1 = adder(1, 2)
# result2 = adder(1, 3, 5, 7, 9)
# result3 = adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(f'result1 : {result1}')
# print(f'result2 : {result2}')
# print(f'result3 : {result3}')
#--------------------------------------------

# 퀴즈
# 함수 정의 -> 함수 이름, 매개변수(원하는 값), return이 있다.
# 함수 호출 -> 결과변수에 return값을 담는다.
# 1부터 원하는 값까지 더해주는 함수

def adder(args):
    total = 0
    for i in range(1, args+1):
        total += i
    return total

x = int(input('원하는 숫자를 입력하세요 : '))
result = adder(x)
print(f'1부터 더한값은 {result}입니다.')
