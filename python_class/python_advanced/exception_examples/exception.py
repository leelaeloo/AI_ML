# Error의 예 (문법 오류)
# print("Lee Tae Soo" -> 괄호가 닫히지 않음 

# Exception의 예 (런타임 오류)
# num = int("abc")    -> ValueError 발생

# 예외 발생 예시들

# try:
#     # 1. 사용자 입력 오류
#     age = int(input("나이를 입력하세요 : ")) # 문자열 입력시 ValuseError

#     # 2. 파일 처리 오류
#     with opne("존재하지_않는_파일.txt", "r") as file: # FileNotFoundError
#         content = file.read()

#     # 3. 계산 오류
#     result = 10 / 0 # ZeroDivisionError

# except Exception as e:
#     print(f"오류가 발생했습니다 : {e}")