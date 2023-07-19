from urllib.parse import urlparse
import requests, os

current_project_path = os.path.dirname(os.getcwd())

def extract_filename_from_url(url):
    # URL을 urlparse를 사용하여 파싱합니다.
    parsed_url = urlparse(url)
    
    # URL에서 경로(path) 부분을 가져옵니다.
    path = parsed_url.path
    
    # 경로(path)를 슬래시("/")를 기준으로 분할하여 리스트로 만듭니다.
    path_parts = path.split('/')
    
    # 리스트의 마지막 요소가 파일명이므로 해당 요소를 반환합니다.
    filename = path_parts[-1]
    return filename

def download_file_from_url(url, save_filename):
    try:
        # HTTP GET 요청을 보내서 파일 데이터를 가져옵니다.
        response = requests.get(url)
        response.raise_for_status()  # 만약 요청이 실패하면 예외를 발생시킵니다.

        # "images" 폴더가 존재하지 않는 경우 생성합니다.
        if not os.path.exists(f"{current_project_path}/images"):
            os.makedirs(f"{current_project_path}/images")

        # 파일 데이터를 "images" 폴더 내에 지정된 경로로 저장합니다.
        with open(os.path.join(f"{current_project_path}/images", save_filename), "wb") as f:
            f.write(response.content)

        print(f"파일 다운로드 완료: {current_project_path}/images/{save_filename}")
    except requests.exceptions.RequestException as e:
        print(f"파일 다운로드 실패: {e}")