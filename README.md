# 인스타그램 크롤러

## Description

태그를 이용하여 이미지를 크롤링합니다. 현재 프로젝트 위치의 images 폴더에 저장됩니다.

## Requirement

-   Python(3.11.4 버전 기준으로 개발함)
-   Chrome & Driver

## How to Start

### Environment Setting

app/env.py 파일을 확인하고 아래 설명을 읽고 변수들을 수정합니다.

-   instagram_username: 인스타그램 아이디
-   instagram_password: 인스타그램 비밀번호
-   target_tag: 크롤링할 태그
-   crawling_count: 크롤링할 이미지 개수

### Example env.py

```python
instagram_username = "test"
instagram_password = "test"
target_tag = "레터링케이크"
crawling_count = 100
```

### ⚠️ Warning ⚠️

1. 정책으로 인해서 인스타그램 계정이 정지될 수 있습니다.
2. 변수를 수정하고 다른사람에게 공유하지 마세요.

### Run

```shell

# 1. 가상환경 생성
python -m venv venv

# 2. 가상환경 실행
source venv/bin/activate

# 3. 필요한 라이브러리 설치
pip install -r requirements.txt

# 4. 크롤링 실행
python app/main.py

```

## License

[MIT](LICENSE)
