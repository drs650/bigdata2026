# # 113p

# # 구구단 2단
# for i in range(1, 10) :
#     print(f'2 x {i} = {i * 2}')

# # 단을 입력받아 구구단 출력
# num = int(input('단 입력 : '))
# for i in range(1, 10) :
#     print(f'{num} x {i} = {i * num}')

# for dan in range(2, 10) :
#     print(f'----{dan}단----')
#     for i in range(1, 10):
#         print(f'{dan} x {i} = {dan * i}')

#-----------------------------------------------------------------------

main = ['베이컨', '크래미']
side = ['당근', '오이']
x = 1
for m in main :
    for s in side :
        print(f'{x}: {m}+{s}+계란')
        x += 1
