# 메소드 오버라이딩을 통한 Polymoriphism(다형성) 구현
# 카드결제, 현금결제, 포인트 결제, 클래스에서 결제 메소드를 오버라이딩하기

class Payment: # 부모클래스 : 결제라는 공통기능 pay()를 정의 
    def pay(self, amount):
        print(f"{amount}원 결재를 진행함")
        # pass - 내용없이 만들수도 있다.

# 이하 자식 클래스
class Cardpayment(Payment): # 카드결제 클래스 : 카드수수료 2%를 계산하여 결제

    def abc():
        print("CardPayment 고유메소드")

    def pay(self, amount): # 메소드 오버라이드 - 강요는 아님 선택적
        fee = amount * 0.02
        total = amount + fee
        print(f"[카드 결제]")
        print(f'상품금액: {amount}원')
        print(f'수수료: {fee}원')
        print(f'최종 결제 금액: {total}원')

class CashPayment(Payment): # 현금결제 클래스 : 현금 할인 5%를 적용하여 결제

    def __init__(self): # 이 코드는 생략가능
        pass

    def pay(self, amount):
        discount = amount * 0.05
        total = amount - discount
        print(f"[현금결제]")
        print(f'상품금액: {amount}원')
        print(f'할인금액: {discount}원')
        print(f'최종 결제 금액: {total}원')

class Pointpayment(Payment): # 포인트 결제 클래스 : 금액만큼 포인트 사용
    def pay(self, amount):
        print(f"[포인트결제]")
        print(f"{amount}포인트를 사용함")

# 클래스 공통 처리함수 : 전달받은 객체의 pay()를 호출
def process_Payment(paymentAddr, amount:int) -> None:
    paymentAddr.pay(amount)

if __name__ == "__main__":

    p1 = Cardpayment()
    p2 = CashPayment()
    p3 = Pointpayment()

    process_Payment(p1, 10000)
    print()
    process_Payment(p2, 10000)
    print()
    process_Payment(Pointpayment(), 10000)
