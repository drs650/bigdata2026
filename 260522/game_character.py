# game_character.py
# 이름: ___________ 날짜: ___________

class Character:
    """게임 캐릭터 클래스"""

    def __init__(self, name, hp, mp, attack, job='모험가', shield=0):
        self.name = name # 캐릭터 이름
        self.hp = hp # 현재 체력
        self.mp = mp # 현재 마나
        self.attack = attack # 공격력
        self.job = job # 직업
        self.shield = shield # 방패 횟수
        self.is_blocking = False # 방패 블록 상태

    def show_info(self):
        # TODO: 캐릭터 정보를 출력하세요 (R-04, R-16)
        print(f"[{self.job}] {self.name} | HP: {self.hp} | MP: {self.mp} | 공격력: {self.attack} | 방패: {self.shield}")

    def attack_enemy(self, target):
        # TODO: target을 공격하는 코드를 만드세요 (R-05, R-06, R-07)
        damage = self.attack
        if target.is_blocking:
            damage = damage // 2
            target.is_blocking = False
        target.hp -= damage
        print(f"{self.name}이(가) {target.name}을(를) 공격! {damage} 피해!")
        if not target.is_alive():
            print(f" ☠️ {target.name}이(가) 쓰러졌다!")

    def is_alive(self):
        # TODO: hp가 0보다 크면 True 반환 (R-08)
        return self.hp > 0

    def shield_block(self):
        # TODO: 방패 기능을 구현하세요 (R-14, R-15)
        if self.shield > 0:
            self.is_blocking = True
            self.shield -= 1
            print(f"{self.name}이(가) 방패를 들었다! (남은 횟수: {self.shield})")
        else:
            print(f"{self.name}: 방패가 없어요! 😢")

 

    def __str__(self):
        return f"{self.job} {self.name} (HP: {self.hp})"


if __name__ == "__main__":
    hero = Character('아서', hp=150, attack=30, job='전사', shield=3)
    enemy = Character('드래곤', hp=200, attack=40, job='몬스터')

    hero.show_info()
    enemy.show_info()
    print("-" * 40)

    hero.shield_block()
    enemy.attack_enemy(hero)
    hero.attack_enemy(enemy)
    hero.attack_enemy(enemy)
    
    print("-" * 40)
    hero.show_info()
    enemy.show_info()