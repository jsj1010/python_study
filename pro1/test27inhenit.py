# 상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
# 코드 재사용 가능
# 확장성 - 기존 클래스에 새기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공동개념은 부모 클래스, 구조적내용은 자식클래스에서 구현
# 다형성 구사 - 메소드 오버라이딩

class Animal:   # 동물들이 가져야할 공통 속성과 행위를 선언
    age = 1

    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 샘물')

# 상속 - Animal : 부모, 조상, super, parent, 상위 클래스
#     -  Dog    : 자식, 자손, sub, child, 파생, 하위클래스

class Dog(Animal):
    def __init__(self):
        print('dog생성자')

    def my(self):
        print('댕댕이라고 해요~~~')

dog1 = Dog()
dog1.my()
dog1.move()
print('age: ', dog1.age)
print()

dog2 = Dog()
dog2.my()
dog2.move()
print('age: ', dog2.age)

print("-----------------------------")
class Horse(Animal):
    pass # 클래스에 멤버가 없음

horse1 = Horse() # 자식의 생성자가 없을 경우 부모 생성자 수행 
horse1.move()




