class Vehicle:
    # 모든 차량의 기본 클래스

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.yaer = year
        self.odometer = 0
        self.fuel = 0

    def fill_fuel_tank(self, amount):
        # 연료 탱크에 주유
        self.fuel += amount
        print(f"{amount}L의 연료를 주유했습니다. 현재 연료 : {self.fuel}L")

