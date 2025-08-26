# 딕셔너리를 활용한 간단한 주소록 프로그램
# 연락처 이름을 키로 하고, 전화번호, 이메일, 주소 등의 정보를 값으로 저장
# 중첩 딕셔너리 구조를 사용하여 각 연락처마다 여러 정보를 저장
# 연락처 추가, 삭제, 검색, 수정, 모든 연락처 보기 기능을 구현

contacts = {}

while True:
    print("\n1. 연락처 추가 2. 연락처 검색 3. 모두 보기 4. 연락처 수정 5. 연락처 삭제 6. 종료")
    choice = input("선택: ")
    
    if choice == '1':  # 연락처 추가
        print("\n=== 연락처 추가 ===")
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("연락처가 추가되었습니다.")
        
    elif choice == '2':  # 연락처 검색
        print("\n=== 연락처 검색 ===")
        name = input("검색할 이름: ")
        if name in contacts:
            print(f"\n이름: {name}")
            print(f"전화번호: {contacts[name]['phone']}")
            print(f"이메일: {contacts[name]['email']}")
            print(f"주소: {contacts[name]['address']}")
        else:
            print("연락처를 찾을 수 없습니다.")
            
    elif choice == '3':  # 모든 연락처 보기
        print("\n=== 전체 연락처 ===")
        if contacts:
            for name, info in contacts.items():
                print(f"\n이름: {name}")
                print(f"전화번호: {info['phone']}")
                print(f"이메일: {info['email']}")
                print(f"주소: {info['address']}")
        else:
            print("저장된 연락처가 없습니다.")
            
    elif choice == '4':  # 연락처 수정
        print("\n=== 연락처 수정 ===")
        name = input("수정할 이름: ")
        if name in contacts:
            phone = input("새 전화번호: ")
            email = input("새 이메일: ")
            address = input("새 주소: ")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("연락처가 수정되었습니다.")
        else:
            print("연락처를 찾을 수 없습니다.")
            
    elif choice == '5':  # 연락처 삭제
        print("\n=== 연락처 삭제 ===")
        name = input("삭제할 이름: ")
        if name in contacts:
            del contacts[name]
            print("연락처가 삭제되었습니다.")
        else:
            print("연락처를 찾을 수 없습니다.")
            
    elif choice == '6':  # 종료
        break