# # 상속
# # --> 부모(슈퍼) 클래스의 코드를 자식(서브) 클래스가 물려받는 것

# class Animal: # 클래스 정의 - 부모(슈퍼) 클래스
#     def __init__(self):
#         self.height = 30 # 인스턴스 변수

#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# fubao = Animal() # 인스턴스(객체) 생성
# fubao.get_height() # 인스턴스 메서드 호출

# class Dog(Animal): # 자식(서브) 클래스 정의 class 자식클래스명(부모클래스명):
#     pass

# class Cat(Animal): # 자식(서브) 클래스 정의
#     pass

# mung = Dog()
# mung.get_height() # 상속받은 인스턴스 메서드 호출

# meow = Cat()
# meow.get_height()

# print(fubao)
# print(mung)
# print(meow)

# -------------------------------------------------------------------------------
# class Animal: # 클래스 정의 - 부모(슈퍼) 클래스
#     def __init__(self):
#         self.height = 30 # 인스턴스 변수

#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# class Dog(Animal):
#     def cry(self):
#         print('멍멍')

# class Cat(Animal):
#     def run(self):
#         print('살금살금')

# fubao = Animal()
# mung = Dog()
# meow = Cat()

# fubao.get_height()
# print('-' * 50)

# mung.get_height()
# mung.cry()
# print('-' * 50)

# meow.get_height()
# meow.run()
# -------------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f'안녕하세요, 저는 {self.name}입니다.')

# class Child(Parent):
#     pass

# person1 = Parent('김슈퍼')
# person1.hello()

# person2 = Child('김서브')
# person2.hello()
# -------------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f'안녕하세요, 저는 {self.name}입니다.')

# class Child(Parent):
#     def bye(self):
#         print(f'{self.name}은 떠납니다.')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브')

# person1.hello()
# print('-' * 50)

# person2.hello()
# person2.bye()
# -------------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f'안녕하세요, 저는 {self.name}입니다.')

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def bye(self):
#         print(f'{self.age}살인 {self.name}은 떠납니다.')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.hello()
# print('-' * 50)

# person2.hello()
# person2.bye()
# -------------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f'안녕하세요, 저는 {self.name}입니다.')

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name) # 부모의 생성자를 호출
#         self.age = age

#     def bye(self):
#         super().hello() # 부모의 인스턴스 메서드를 호출
#         print(f'{self.age}살인 {self.name}은 떠납니다.')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.hello()
# person2.bye()
# -------------------------------------------------------------------------------
class Car: # 부모(슈퍼) 클래스
    max_oil = 50 # 클래스 변수 --> 최대 주유량

    def __init__(self, oil):
        self.oil = oil # 인스턴스 변수 --> 현재 기름량

    def add_oil(self, oil):
        if oil <= 0 : # 0이하의 주유는 진행하지 않는다.
            return # 함수 종료
        self.oil += oil # oil만큼 기름 넣는다.
        if self.oil > self.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유 상태: {self.oil}')

car1 = Car(20)
car1.car_info()
car1.add_oil(40)
car1.car_info()

class Hybrid(Car):
    max_battery = 30 # 최대 배터리 충전량 --> 클래스 변수

    def __init__(self, oil, battery): # 자식의 생성자
        super().__init__(oil) # 부모의 생성자를 호출
        self.battery = battery # 인스턴스 변수

    def charge(self, battery): # 인스턴스 메서드 정의
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info() # 부모의 메서드 호출
        print(f'현재 충전 상태: {self.battery}')

car2 = Hybrid(10, 5)
car2.add_oil(30)
car2.charge(15)
car2.hybrid_info()