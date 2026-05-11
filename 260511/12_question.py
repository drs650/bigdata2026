# import random

# com = random.randint(1, 30) # 1~30 중 하나의 정수 추출
# print('<< 1~30 숫자 맞히기 게임>>')
# while True:
#     player = int(input('숫자 입력(종료0): '))
#     if player == 0:
#         break
#     elif player == com:
#         print('정답')
#         break
#     elif player > com:
#         print('더 작은 숫자 입력')
#     else:
#         print('더 큰 숫자 입력')

# import random

# lotto = [] # 빈 리스트
# while True:
#     num = random.randint(1, 45) # 1~45 정수 중에서 하나 추출
#     if num not in lotto: # 중복이 되지 않았다.
#         lotto.append(num)
#     if len(lotto) == 6: # len(리스트 또는 문자열) -> 총 개수(총 글자 수)
#         break

# print('<< 생성된 로또 번호 >>')
# for i in range(6):
#     print(f'{lotto[i]}', end=' ')
# print()

# # random.sample(범위, 개수) -> 범위에서 개수만큼 중복되지 않는 수를 추출
# lotto2 = random.sample(range(1, 46), 6)
# for i in range(6):
#     print(f'{lotto2[i]}', end=' ')


# #8
# vote = {'대성리':0,
#         '춘천':0,
#         '을왕리':0,
#         '청평':0
#         }
# for key in vote:
#     print(f'{key}:{vote[key]}표', end=' ')
# print('\n')
# print('<< MT 장소 투표 >>')

#10
# def price(menue):
#     if menue == 1:
#         m = '아메리카노'
#         p = 3000
#     elif menue == 2:
#         m = '카페라떼'
#         p = 4000
#     elif menue == 3:
#         m = '바닐라라떼'
#         p = 4500
#     print(f'{m}: {p:,}원') # 천 단위 구분 기호 추가

# menue = int(input('메뉴선택(1: 아메리카노/ 2: 카페라떼/ 3: 바닐라라떼) '))
# price(menue)

#11
files = ['report.hwp', 'newJeans', 'attention.png', 'ditto.jpg', 'address.xslx']

result = filter(lambda x : 'jpg' in x or 'png' in x, files)
print(list(result))
