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
        self.author = author

    def display(self):
        print(f'작성자: {self.author} \n제목: {self.title} \n내용: {self.content}')


# ----- 코드 실행 ------
members = [
    Member("김한규", "kim1", "1234"),
    Member("서영환", "seo1", "1234"),
    Member("김동민", "kim2", "1234")
]

posts = [
    Post("text1", "text.", "kim1"),
    Post("text2", "text.", "kim1"),
    Post("text3", "text.", "kim1"),
    Post("text4", "text.", "seo1"),
    Post("text5", "text.", "seo1"),
    Post("text6", "text.", "seo1"),
    Post("text7", "text.", "kim2"),
    Post("text8", "texttext.", "kim2"),
    Post("text9", "texttext.", "kim2")
]

# 회원목록 출력
print("회원 목록:")
for member in members:
    member.display()

# 특정조건 검색

username = "kim1"
print(f"{username} 작성 게시물:")
for post in posts:
    if post.author == username:
        print(post.title)

keyword = "text"
print(f"'{keyword}' 포함된 게시물:")
for post in posts:
    if keyword in post.content:
        print(post.title)

# TODO : 코드 구현이 필요합니다.


# commnd control code
print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
print("{0:^40}".format("퍼스트 코팅 : 회원과 게시물을 관리"))
print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
main_pointer = input("회원 관리(1)\n게시물 관리(2)\n종료(3)\n이동 하시려는 곳을 입력해주세요 : ")
print_content = [
    ['회원 이름:', '회원 아이디:', '회원 비밀번호:', '회원'],
    ['게시물 제목:', '게시물 내용:', '작성자:', '게시물']
]
print_title = [
    ['회원 등록', '회원 목록', '회원 이름 검색', '회원 아이디 검색'],
    ['게시물 등록', '게시물 목록', '게시물 제목 검색', '게시물 아이디 검색']
]
while main_pointer != '3':
    checks = int(main_pointer) - 1
    if main_pointer != '1' and main_pointer != '2' and main_pointer != '3':
        # 1~3 까지의 숫자만 입력 받기에 그 외 입력시 다시 입력 받기
        print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")
        continue
    # sub_pointer의 input 부분이 길어짐에 따라 길이를 줄이기 위해 show_title 변수 선언
    show_title = print_content[checks][3]
    print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
    sub_pointer = input(
        f"{show_title} 생성(1)\n{show_title} 목록(2)\n{show_title} 이름 검색(3)\n{show_title} 아이디 검색(4)\n메인이동(5)"
        f"\n이동 하시려는 곳을 입력해주세요 : ")
    while sub_pointer != '5':
        # 생성 시 member_info 혹은 post_info 변수가 변경 되므로 밖이 아닌 안에 두어 업데이트 감지
        if main_pointer == '1':
            all_print = members
        else:
            all_print = posts
        # 현재 위치의 타이틀을 \t\t\t 후 중앙 정렬 하여 노출
        checks2 = int(sub_pointer) - 1
        if int(sub_pointer) <= 4:
            print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
            print("{0:^40}".format(print_title[checks][checks2]))
            print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))

        if sub_pointer == '1':
            # Member 등록 or Post 생성
            a = input(f"{print_content[checks][0]}")
            if checks == 0:
                while True:
                    b = input(f"{print_content[checks][1]}")
                    if any(member.username == b for member in members):
                        print("중복된 아이디입니다. 다른 아이디를 입력해주세요.")
                    else:
                        break
            else:
                b = input(f"{print_content[checks][1]}")
            c = input(f"{print_content[checks][2]}")
            # Member 등록 or Post 생성 예외 처리 부분 작성 필요
            change_ok = True
            if main_pointer == '1':
                members.append(Member(a, b, c))
            else:
                posts.append(Post(a, b, c))

        elif sub_pointer == '2':
            # Member or Post 전체를 가져와 출력
            print(f"총 {len(all_print)}건이 있습니다.")
            for value in all_print:
                print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
                value.display()
            print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
        elif sub_pointer == '3':
            # Member의 이름 or Post의 제목 에 입력한 값이 포함 되면 출력
            search_value = input(
                f"찾는 {print_content[int(main_pointer) - 1][0]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.name) or (
                        main_pointer == '2' and search_value in value.title):
                    print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
                    value.display()
        elif sub_pointer == '4':
            # Member의 아이디 or Post의 내용 에 입력한 값이 포함 되면 출력
            search_value = input(
                f"찾는 {print_content[int(main_pointer) - 1][2]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.username) or (
                        main_pointer == '2' and search_value in value.author):
                    value.display()
        elif sub_pointer != '5':
            # 1~5 까지의 숫자만 입력 받기에 그 외 입력시 다시 입력 받기
            print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        sub_pointer = input(
            f"{show_title} 생성(1)\n{show_title} 목록(2)\n{show_title} 이름 검색(3)\n{show_title} 아이디 검색(4)\n메인이동(5)"
            f"\n이동 하시려는 곳을 입력해주세요 : ")
    print("{0:═^40}".format(" ೋღ 🌺 ღೋ "))
    main_pointer = input("회원 관리(1)\n게시물 관리(2)\n종료(3)\n이동 하시려는 곳을 입력해주세요 : ")
