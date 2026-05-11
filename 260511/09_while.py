# hp = 100 # 체력
# while hp > 0: # 체력이 0보다 크면 계속 반복
# 	print(f'주인공의 체력은 {hp}입니다.')
# 	damage = int(input('얼마의 데미지를 입힐까요?'))
# 	# 체력 - 데미지 --> 남은 체력
# 	hp -= damage
	
# print('주인공의 체력이 0이 되었으므로 게임을 종료합니다.')

# 114p
# while True:
#     num = int(input('번호 입력(종료 0) : '))
#     if num == 0:
#         break # 무조건 반복문 종료
#     print('while 무한루프 반복중')

# continue --> 이번 차례는 건너뛰고 계속 진행
# 1~30 사이의 정수 중에서 7의 배수 출력
for x in range(1, 31):
    if x % 7 != 0:
        continue
    print(f'7의 배수 : {x}')