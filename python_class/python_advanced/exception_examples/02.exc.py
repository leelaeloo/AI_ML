class MyCustomError(Exception):
    pass

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

class InsufficientFundError(Exception):
    pass

    def __init__(self, balance, amount, message=None):
        self.balance = balance
        self.amount = amount
        self.message = message or f"잔액 부족 : 현재 잔액{balance}원, 요청 금액 {amount}원"
        super().__init__(self.message)

    def get_deficit(self):
        return self.amount - self.balance

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금 금액은 양수여야 합니다.")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("출금 금액은 양수여야 합니다.")
        if amount  > self.balance:
            raise InsufficientFundError(self.balance, amount)
        self.balance -= amount
        return self.balance

# 예외 처리 예시
account = BankAccount("이태수", 15000)

try:
    account.withdraw(20000)
except InsufficientFundError as e:
    print(e)
    # 출력: 잔액 부족: 현재 잔액 15000원, 요청 금액 20000원
    deficit = e.get_deficit()
    print(f"부족한 금액: {deficit}원")
    # 출력: 부족한 금액: 5000원