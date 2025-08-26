# 집합 예제 (두 반 학생들의 취미 분석)

# 두 반 학생들의 취미 분석
class_a_hobbies = {"축구", "농구", "게임", "노래", "달리기"}
class_b_hobbies = {"야구", "농구", "게임", "볼링", "음악", "배드민턴"}

# 양쪽 반에 모두 있는 취미 -> 교집합
common_hobbies = class_a_hobbies & class_b_hobbies
print(f"공통 취미 : {common_hobbies}")                  # {'게임', '농구'}

# A반에만 있는 취미 -> 차집합
only_a_hobbies = class_a_hobbies - class_b_hobbies
print(f"A반 전용 취미 : {only_a_hobbies}")             # A반 전용 취미 : {'축구', '노래', '달리기'}

# B반에만 있는 취미 -> 차집합
only_b_hobbies = class_b_hobbies - class_a_hobbies
print(f"B반 전용 취미 : {class_b_hobbies}")            # B반 전용 취미 : {'볼링', '게임', '야구', '배드민턴', '농구', '음악'}

# 모든 취미 목록 -> 합집합
all_hobbies = class_a_hobbies | class_b_hobbies
print(f"모든 취미 목록 : {all_hobbies}")               # 모든 취미 목록 : {'축구', '배드민턴', '노래', '볼링', '게임', '야구', '달리기', '농구', '음악'}

# 고유한 취미 -> 대칭 차집합
unique_hobbies = class_a_hobbies ^ class_b_hobbies
print(f"한쪽 반에만 있는취미 : {unique_hobbies}")     # 한쪽 반에만 있는취미 : {'축구', '배드민턴', '노래', '볼링', '야구', '달리기', '음악'}

# 취미의 종류 수
print(f"전체 취미 종류 수 : {len(all_hobbies)}종류")      # 전체 취미 종류 수 : 9종류