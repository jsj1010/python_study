# 냉장고 객체에 음식개체 저장하기

class FoodData: # 음식 객체 (냉장고 보관될 클래스)
    def __init__(self, name, expiry_data):
        self.name = name
        self.expiry_data = expiry_data

class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문이 열림')

    def close(self):
        self.isOpened = False
        print('냉장고 문이 닫힘')


    def foodList(self): # 냉장고 문이 열린 경우 음식물 확인 메소드
        for f in self.foods:
            print(f" - {f.name} {f.expiry_data}")
        print()

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고의 {thing.name} 넣음")
            self.foodList()
        else:
            print("냉장고 문이 닫혀있음")

fobj = Fridge()

apple = FoodData("사과", "2026-9-6")
fobj.put(apple) # 냉장고 문이 닫혀있음.
fobj.open()
fobj.put(apple)
fobj.close()

print()
cola = FoodData("콜라", "2027-5-5")
fobj.put(cola)
fobj.open()
fobj.put(cola)
fobj.close()