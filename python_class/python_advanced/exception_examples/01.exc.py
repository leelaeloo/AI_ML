class InsufficientFundsError(Exception):
    # 계좌에 잔액이 부족할 때 발생하는 예외


    def __init__(self, balance, amount, message=None):
        self.balance = balance
        self.amount = amount
        self.message = message or f"잔액 부족 : 현재 잔액 {balance}원, 요청 금액 {amount}원"
        super().__init__(self.message)

    
    def get_deficit(self):
        # 부족한 금액 계산
        return self.amount - self.balance


