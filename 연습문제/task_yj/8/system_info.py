import os
import sys

def system_info():
    
    print("현재 작업 디렉토리:", os.getcwd())
    print("Python 버전:", sys.version.splitlines()[0])
    print("운영체제:", os.name)
    path_env = os.getenv('PATH')
    if path_env:
        separator = os.pathsep
        path_parts = path_env.split(separator)[:3]
        print("환경 변수 PATH 일부:", ":".join(path_parts))
    else:
        print("환경 변수 PATH를 찾을 수 없습니다.")

    print("파일 경로 정보:")
    example_path = os.path.join(os.path.expanduser("~"), "documents", "report.txt")
    print(f"- 디렉토리: {os.path.dirname(example_path)}")
    print(f"- 파일명: {os.path.basename(example_path)}")
    print(f"- 확장자: {os.path.splitext(example_path)[1]}")
    print(f"파일 존재 여부: {os.path.exists(example_path)}")

system_info()