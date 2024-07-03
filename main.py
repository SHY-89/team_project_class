# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름 : {self.name}\n아이디 : {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f'제목: {self.title} \n내용: {self.content}')


# ----- 코드 실행 ------
members = []
posts = []

# TODO : 코드 구현이 필요합니다.
