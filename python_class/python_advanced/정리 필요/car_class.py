class Car:
    wheels = 4
    
    def __init__(self, make, model, year, color):
        # 인스턴스 변수 (각 객체마다 다름)
        self.make = make        # 제조사
        self.model = model      # 모델명
        self.year = year        # 연식
        self.color = color      # 색상
        self.speed = 0          # 현재 속도
        self.odometer = 0       # 주행 거리

    def accelerate(self, speed_increase):
        # 속도 증가
        self.speed += speed_increase
        print(f"속도가 {speed_increase}km/h 증가했습니다. \n현재 속도 : {self.speed}km/h")

    def brake(self, speed_decrease):
        # 속도 감소
        if self.speed < speed_decrease:
            self.speed = 0
        else:
            self.speed -= speed_decrease
        print(f"속도가 {speed_decrease}km/h 감소했습니다. \n현재 속도 : {self.speed}km/h")

    def drive(self, distance):
        # 주어진 거리만큼 주행
        if self.speed > 0:
            self.odometer += distance
            print(f"속도가 {distance}km/h 주행했습니다. \n총 주행거리 : {self.odometer}km")
        else:
            print("차가 정지해 있어 주행할 수 없습니다.")

    def get_description(self):
        # 자동차에 대한 설명을 반환
        return f"{self.year}년식 {self.color}색 {self.make} {self.model}"
    
# Car 클래스 객체 생성
my_car = Car("현대", "쏘k나타", 2020, "검정")
your_car = Car("기아", "K5", 2022, "흰")

# 객체의 속성 접근
print(f"나의 차 : {my_car.get_description()}")
print(f"상대 차 : {your_car.get_description()}")
print(f"모든 차는 : {Car.wheels}개의 바퀴를 가집니다.") # -> 클래스 변수 접근

# 메서드 호출
my_car.accelerate(30)   # 속도가 30km/h 증가
my_car.drive(10)        # 10km를 주행
my_car.brake(10)        # 속도가 10km/h 감소

# 객체마다 독립적인 상대를 가짐
your_car.accelerate(50)     # 속도가 50km/h 증가
print(f"나의 차 : {my_car.speed}km/h")      # 20km/h
print(f"상대 차 : {your_car.speed}km/h")    # 50km/h