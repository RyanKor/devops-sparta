# 베이스 이미지로 Python 3.11 Slim 버전 사용
FROM python:3.11-slim

# 작업 디렉토리를 설정
WORKDIR /app

# FastAPI 및 uvicorn 설치를 위한 필수 라이브러리
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치를 위한 pip 업그레이드
RUN pip install --upgrade pip

# FastAPI 및 uvicorn 설치
RUN pip install fastapi==0.113.0 uvicorn

# 애플리케이션 소스 코드 복사
COPY 02-fastapi/main.py /app/main.py

# 컨테이너가 실행될 때 기본적으로 uvicorn으로 FastAPI 앱 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
