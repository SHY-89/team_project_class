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
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        super().__init__(username)

    def display(self):
        print(f'작성자: {self.username} \n제목: {self.title} \n내용: {self.content}')

    # ----- 코드 실행 ------


members = []
posts = []

# TODO : 코드 구현이 필요합니다.
