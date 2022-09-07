# 📎 목차

1. [게시글 crud api 서비스]
2. [개발 기간]
3. [요구사항 및 분석]
4. [기술 스택]
5. [API Endpoints]


# 🚀 게시글 crud api 서비스

# 📆 개발 기간
- 2022.09.06 ~ 2022.09.07


# 📝 요구사항 및 분석
### 1. 게시물 올리기

-  제목과 본문으로 구성 됨
- 제목은 최대 20자, 본문은 200자로 제한
- 제목과 본문 모두 이모지 포함

### 2. 게시물 올릴 때 비밀번호 설정

- 추후 본인이 작성한 게시물에 비밀번호 입력 후 수정, 삭제 가능
- 회원가입, 로그인 없이 비밀번호만 일치하면 수정, 삭제 가능
- 비밀번호는 데이터베이스에 암호화된 형태로 저장되어야 함
- 비밀번호는 6자 이상, 숫자 1개 이상 반드시 포함되어야 함

### 3. 게시물 조회

- 모든 사용자는 한 페이지 내에서 모든 게시물을 최신 글 순서로 확인 할 수 있어야 함
- 게시글의 개수가 많을 때, 추가 로드는 20개 단위


# 🛠 기술 스택
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# 🎯 API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /posting/ | GET | 게시글 조회하기 | page: int | title: string, content: string |
| /posting/ | POST | 게시글 등록하기 | title: string, content: string, password: string | 성공 여부 |
| /posting/update/ | PUT | 게시글 수정하기 | id: int, title: string, content: string, password: string | 성공 여부 |
| /posting/delete/ | DELETE | 게시글 삭제하기 | id: int, password: string | 성공 여부 |