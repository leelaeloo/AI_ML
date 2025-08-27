# 클래스 과제
# 다음 클래스 구현
# Book : 도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리
# Library : 도서 컬렉션을 관리하고 대출/반납 기능 제공
# Member : 도서관 회원 정보와 대출 목록 관리

# 다음 기능 구현
# 도서 추가/삭제
# 도서 검색(제목, 저자, ISBN으로)
# 회원 등록/관리
# 회원별 대출 현황 확인

# 객체 지향 설계 원칙(SOLID)을 최소한 2가지 이상 적용
# 적절한 캡슐화를 통해 데이터 보호

# Book 클래스
class Book:
    """도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리하는 클래스"""
    def __init__(self, title, author, isbn, year_of_publication, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_of_publication = year_of_publication
        self.is_available = is_available

    def __repr__(self):
        return f"Book(제목: {self.title}, 저자: {self.author}, ISBN: {self.isbn}, 출판연도: {self.year_of_publication})"

# Member 클래스
class Member:
    """도서관 회원 정보와 대출 목록을 관리하는 클래스"""
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __repr__(self):
        return f"Member(이름: {self.name})"

# Library 클래스
class Library:
    """도서 컬렉션 관리 및 대출/반납 기능 제공"""
    def __init__(self):
        self.books = []
        self.members = []

    # 도서 추가
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' 도서가 추가되었습니다.")

    # 도서 삭제
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book.title}' 도서가 삭제되었습니다.")
        else:
            print("도서관에 해당 도서가 없습니다.")

    # 회원 등록
    def register_member(self, member):
        self.members.append(member)
        print(f"'{member.name}'님이 회원으로 등록되었습니다.")

    # 도서 검색
    def search_book(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == book.isbn]
        return results

    # 도서 대출
    def borrow_book(self, member, book):
        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"'{book.title}'을(를) '{member.name}'님이 대출했습니다.")
        else:
            print(f"'{book.title}'은(는) 현재 대출 불가능합니다.")

    # 도서 반납
    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"'{book.title}'을(를) '{member.name}'님이 반납했습니다.")
        else:
            print(f"'{member.name}'님의 대출 목록에 '{book.title}'이(가) 없습니다.")
            
    # 회원별 대출 현황 확인
    def get_borrowed_status(self, member):
        print(f"'{member.name}'님이 빌린 책:")
        if not member.borrowed_books:
            print("대출한 책이 없습니다.")
        else:
            for book in member.borrowed_books:
                print(f"- {book.title} (by {book.author})")

# --- 실행 예시 ---
if __name__ == "__main__":
    my_library = Library()

    book1 = Book("개미", "베르나르 베르베르", "978-89-329-0797-0", 1991)
    book2 = Book("개미의 날", "베르나르 베르베르", "978-89-329-0798-7", 1992)

    member1 = Member("이태수")
    member2 = Member("삼ㅁ태수")
    member3 = Member("이태수")
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.register_member(member1)

    print("-" * 20)

    # 대출 및 현황 확인
    my_library.borrow_book(member1, book1)
    my_library.get_borrowed_status(member1)
    
    print("-" * 20)
    
    # 반납 및 현황 확인
    my_library.return_book(member1, book1)
    my_library.get_borrowed_status(member1)
    
    print("-" * 20)
    
    # 도서 검색
    search_results = my_library.search_book("베르베르")
    print("도서 검색 결과:")
    for book in search_results:
        print(f"- {book.title} (by {book.author})")
    
    print("-" * 20)
    
    # 도서 삭제
    my_library.remove_book(book2)


        