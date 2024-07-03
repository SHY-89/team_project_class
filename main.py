# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

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


# ----- 코드 실행 ------
members = []
posts = []

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
        # 1~3 까지의 숫자만 입력 받기에 그 외 입력시 다시 입력 받기
        print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")
        continue
    show_title = print_content[checks][3]

    sub_pointer = input(f"{show_title} 생성(1)/{show_title} 목록(2)/{show_title} 이름 검색(3)/{show_title} 아이디 검색(4)/메인이동(5) : ")
    while sub_pointer != '5':
        # 생성 시 member_info 혹은 post_info 변수가 변경 되므로 밖이 아닌 안에 두어 업데이트 감지
        if main_pointer == '1':
            all_print = member_info
        else:
            all_print = post_info

        if sub_pointer == '1':
            # Member 등록 or Post 생성
            a = input(f"{print_content[int(main_pointer)-1][0]}")
            b = input(f"{print_content[int(main_pointer)-1][1]}")
            c = input(f"{print_content[int(main_pointer)-1][2]}")
            # Member 등록 or Post 생성 예외 처리 부분 작성 필요
            change_ok = True
            if main_pointer == '1':
                member_info.append(Member(a,b,c))
            else:
                post_info.append(Post(a, b, c))

        elif sub_pointer == '2':
            # Member or Post 전체를 가져와 출력
            for value in all_print:
                value.display()
        elif sub_pointer == '3':
            # Member의 이름 or Post의 제목 에 입력한 값이 포함 되면 출력
            search_value = input(f"찾는 {print_content[int(main_pointer)-1][0]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.name) or (main_pointer == '2' and search_value in value.title):
                    value.display()
        elif sub_pointer == '4':
            # Member의 아이디 or Post의 내용 에 입력한 값이 포함 되면 출력
            search_value = input(f"찾는 {print_content[int(main_pointer) - 1][1]}")
            for value in all_print:
                if (main_pointer == '1' and search_value in value.username) or (main_pointer == '2' and search_value in value.content):
                    value.display()
        elif sub_pointer != '5':
            # 1~5 까지의 숫자만 입력 받기에 그 외 입력시 다시 입력 받기
            print("잘 못 입력 하였 습니다. 다시 입력 해 주세요.")
        sub_pointer = input(f"{show_title} 생성(1)/{show_title} 목록(2)/{show_title} 이름 검색(3)/{show_title} 아이디 검색(4)/메인이동(5) : ")
    main_pointer = input("회원 관리(1)/게시물 관리(2)/종료(3) : ")