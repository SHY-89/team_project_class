# team_project_class
회원과 게시물을 관리

요구사항

    Member 클래스 정의
        - 변수
            - 회원 이름 (name)
            - 회원 아이디 (username)
            - 회원 비밀번호 (password)
        - 함수
            - display : 회원 정보를 print, 회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됨
            
    Post 클래스 정의
        - 변수
            - 게시물 제목 (title)
            - 게시물 내용 (content)
            - 작성자 (author) : 회원의 `username` 이 저장
        - 함수
            - display : 게시물 정보를 print

    - 회원 인스턴스를 세개 이상 만들고 members 라는 빈리스트에 append를 써서 저장
	- members 리스트를 돌면서 회원들의 이름을 모두 프린트
    - 각각의 회원이 게시글을 세개 이상 작성
    - 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장
	- for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트
	- for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트


추가 요구사항

    - input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널 조작
    - post도 터미널에서 생성
    - hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장

개발환경 & 사용기술

    Python 3.8.6
    hashlib

개발사항

	- Member class 개발 대기
	- Post class 개발 대기
	- 추가 요구사항 개발 대기
