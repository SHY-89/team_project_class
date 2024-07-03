import hashlib

# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"이름 : {self.name}\n아이디 : {self.username}")


# Post 클래스
class Post(Member):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author= author
        
    def display(self):
        print(f'작성자: {self.author} \n제목: {self.title} \n내용: {self.content}')

# 회원 추가
def add_member(name, username, password):
    member = Member(name, username, password)
    members.append(member)

def add_post(title, content, author_username):
    # 회원 목록 확인
    author = next((member for member in members if member.username == author_username), None)
    if author:
        post = Post(title, content, author.name)
        posts.append(post)
        print(f"'{title}' 등록완료")
    else:
        print("회원등록필요.")

# ----- 코드 실행 ------
members = []
posts = []

# 회원 인스턴스 추가
add_member("김한규", "kim1", "1234")
add_member("서영환", "seo1", "1234")
add_member("김동민", "kim2", "1234")

# 회원목록 출력
print("회원 목록:")
for member in members:
    member.display()

# 게시물 추가
add_post("text", "text.", "kim1")
add_post("text", "text.", "kim1")
add_post("text", "text.", "kim1")

add_post("text", "text.", "seo1")
add_post("text", "text.", "seo1")
add_post("text", "text.", "seo1")

add_post("text", "text.", "kim2")
add_post("text", "text.", "kim2")
add_post("text", "text.", "kim2")


#특정조건 검색

def print_user(username):
    print(f"{username} 작성 게시물:")
    for post in posts:
        if post.author == username:
            print(post.title)

print_user("김한규")


def print_keyword(keyword):
    print(f"'{keyword}' 포함된 게시물:")
    for post in posts:
        if keyword in post.content:
            print(post.title)

print_keyword("text")


# TODO : 코드 구현이 필요합니다.


# commnd control code
print("════════════ ೋღ 🌺 ღೋ ════════════")
print("\t퍼스트 코팅 : 회원과 게시물을 관리")
print("════════════ ೋღ 🌺 ღೋ ════════════")
main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")
member_info = []
post_info = []
while main_pointer != '3':
    print_content =[
        ['회원 이름:', '회원 아이디:', '회원 비밀번호:', '회원'],
        ['게시물 제목:', '게시물 내용:', '작성자:', '게시물']
    ]
    checks = int(main_pointer)-1
    if main_pointer != '1' and main_pointer != '2' and main_pointer != '3':
        print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")
        continue

    sub_pointer = input(f"{print_content[checks][3]} 생성(1)/{print_content[checks][3]} 목록(2)/{print_content[checks][3]} 이름 검색(3)/{print_content[checks][3]} 아이디 검색(4)/메인이동(5) : ")
    while sub_pointer != '5':
        if main_pointer == '1':
            all_print = member_info
        else:
            all_print = post_info
        if sub_pointer == '1':
            a = input(f"{print_content[int(main_pointer)-1][0]}")
            b = input(f"{print_content[int(main_pointer)-1][1]}")
            c = input(f"{print_content[int(main_pointer)-1][2]}")
            change_ok = True
            if main_pointer == '1':
                member_info.append(Member(a,b,c))
            else:
                post_info.append(Post(a, b, c))

        elif sub_pointer == '2':
            for value in all_print:
                value.display()
        elif sub_pointer == '3':
            search_value = input(f"찾는 {print_content[int(main_pointer)-1][0]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.name) or (main_pointer == '2' and search_value in value.title):
                    value.display()
        elif sub_pointer == '4':
            search_value = input(f"찾는 {print_content[int(main_pointer) - 1][1]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.username) or (main_pointer == '2' and search_value in value.content):
                    value.display()
        elif sub_pointer != '5':
            print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        sub_pointer = input(f"{print_content[checks][3]} 생성(1)/{print_content[checks][3]} 목록(2)/{print_content[checks][3]} 이름 검색(3)/{print_content[checks][3]} 아이디 검색(4)/메인이동(5) : ")
    main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")