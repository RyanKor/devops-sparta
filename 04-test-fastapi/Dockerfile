# Stage 1: Build Stage
FROM python:3.11-slim AS build-stage

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
	curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

COPY ./main.py /app/main.py

# Stage 2: Final Stage
# 가볍고 필요한 라이브러리만 포함한 최종 이미지 생성
FROM python:3.11-slim AS final-stage

# 작업 디렉토리를 설정
WORKDIR /app

# Build Stage에서 설치한 Python 라이브러리 복사
COPY --from=build-stage /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin

# 애플리케이션 소스 코드 복사
COPY --from=build-stage /app/main.py /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
