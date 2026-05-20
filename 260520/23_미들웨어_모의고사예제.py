def make_coffee(menu, quantity):
    print(f"☕{menu}{quantity}잔 제조를 시작합니다!")


# ↓ 여기서부터 작성하세요

def check_menu(menu):
    if menu == '아메리카노' or '카페라떼' or '카푸치노':
        print(f'[메뉴확인] 주문 가능한 메뉴입니다.')
        return True
    else:
        print(f'[메뉴확인] 주문 불가능한 메뉴입니다.')
        return False


def check_quantity(quantity):
    if (quantity < 1 or quantity > 10):
        print(f'[수량확인] 수량은 1잔 이상 10잔 이하만 가능합니다.')
        return False
    else:
        print(f'[수량확인] 주문 수량이 유효합니다.')
        return True



if __name__ == "__main__":
    menu = input('주문할 메뉴를 입력하세요: ')
    quantify = int(input('수량을 입력하세요: '))
    if check_menu(menu):
        if check_quantity(quantify):
            make_coffee(menu, quantify)
        

