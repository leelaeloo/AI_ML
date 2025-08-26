PI = 3.14159

# 변수 정의
def add(a, b):
    # 두 수의 합을 반환
    return a + b

def subtract(a, b):
    # 첫 번째 수에서 두 번재 수를 뺀 결과 반환
    return a - b

def multiply(a, b):
    # 두 수의 곱을 반환
    return a * b

def divide(a, b):
    # 첫 번째 수를 두 번째 수로 나눈 결과 반환
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

# 클래스 정의

class Circle:
    # 원을 표현하는 클래스
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        #원의 넓이 계산
        return PI * self.radius ** 2
    
    def circumference(self):
        # 원의 둘레 계산
        return 2 * PI * self.radius