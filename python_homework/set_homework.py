# 소셜 네트워크에서 사용자 간의 관계와 추천 시스템을 구현하는 프로그램 작성
# 공통 관심사를 갖는 친구 응답
# 공통 관심사가 없는 친구 응답

friends_interests = {
    "Alice": {"음악", "영화", "독서"},
    "Bob": {"스포츠", "여행", "음악"},
    "Charlie": {"프로그래밍", "게임", "영화"},
    "David": {"요리", "여행", "사진"},
    "Eve": {"프로그래밍", "독서", "음악"},
    "Frank": {"스포츠", "게임", "요리"},
    "Grace": {"영화", "여행", "독서"}
}

# 분석할 친구 입력
target_friends_name = "ddong"

# 결과 저장용 리스트와 딕셔너리
common_friends = {}
no_common_friends = []

# 입력한 친구가 데이터에 있는지 확인
if target_friends_name not in friends_interests:
    print(f"'{target_friends_name}' 친구를 찾을 수 없습니다.. \n 정확한 친구 이름을 입력해 주세요! " ) 
else:
    target_interests = friends_interests[target_friends_name]

    # 모든 친구를 한 번만 반복
    for friend, interests in friends_interests.items():
        if friend == target_friends_name:
            continue

        # 교집합 연산으로 공통 관심사 찾기
        common = target_interests & interests
        
        # 결과 분류 if/else
        if common:
            common_friends[friend] = common 
        else:
            no_common_friends.append(friend) 

    print(f"\n## {target_friends_name}와 공통 관심사가 있는 친구 ##\n")
    for friend, common in common_friends.items():
        print(f"- {friend}: {common}")

    print(f"\n## {target_friends_name}와 공통 관심사가 없는 친구 ##\n")
    for friend in no_common_friends:
        print(f"- {friend}")