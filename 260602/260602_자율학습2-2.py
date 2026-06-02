
subjects = []

while True:
    print("1.수강 강좌정보 입력 2.평균평점 확인 3. 졸업여건 확인 0.종료 : ", end="")
    num = int(input())

    if num == 0:
        print(f'초간단 평점평균 계산 시스템 종료!')
        break

    elif num == 1:
        print(f'< 수강 강좌정보 입력 >')
        while True:
            sub = input('과목명 (0: 종료) ')
            if sub == '0':
                print(f'< 수강 강좌정보 입력 종료 >\n')
                break
            else:
                count = int(input('학점 수 : '))
                grade = input('취득학점(A,B,C,F) : ')

                info = {
                    '과목명': sub,
                    '학점수': count,
                    '취득학점': grade
                }
                subjects.append(info)
    
    elif num == 2:
        print(f'< 수강 강좌 목록 > ')
        print(f'과목명  학점수  학점')
        print('-' * 20)

        total_count = 0
        total_grade = 0.0

        for s in subjects:
            a, b, c = s.values() 
            print(f'{a}\t {b}\t{c}')

            if c == 'A':
                score = 4.5
            elif c == 'B':
                score = 3.5
            elif c == 'C':
                score = 2.5
            else:
                score = 0.0
            
            total_count += b
            total_grade += b * score

        avg = total_grade / total_count
        print(f'평균평점 : {avg:.2f}\n')
    
    elif num == 3:
        total_reg = int(input('총 등록 학기수 입력: '))
        if total_reg >= 8 :
            print('졸업학기 충족')
        else:
            print(f'{8-total_reg}학기 부족\n')
                  
        total_fin = int(input('수강 완료 학점수 입력: '))
        if total_fin >= 120:
            print(f'졸업학점 충족')
        else:
            print(f'{120-total_fin}학점 부족\n')
        total_avg = float(input('총 평균 평점 입력: '))
        if total_avg >= 2.5:
            print('졸업 평균평점 충족')
        else:
            print(f'{2.5-total_avg:.2f} 평균평점 낮음')
    