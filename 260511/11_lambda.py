# 람다 표현식
# <형식>
# lambda 매개변수들 : 식

# 1) def
def plus_five(x):
    return x + 5

result = plus_five(10)
print(result)

# 2) lambda
result_plus_five = lambda x : x + 5
result2 = result_plus_five(10)
print(result2)

# 람다 표현식을 인수로 사용
# lambda x : x + 10
# map(함수, 시퀀스 자료형)
result = map(lambda x : x + 10, [30, 20, 10])
print(list(result))


result3 = filter(lambda x : x < 20, [30, 20, 10]) # 참(True)인것만
print(list(result3))