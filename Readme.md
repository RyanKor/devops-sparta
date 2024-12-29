# DevOps Lecture for Team Sparta

- Dockerhub 레지스트리 확인하기 : [링크](https://hub.docker.com/repository/docker/ryankor/devops-sparta/general)

## 각 챕터별 학습 자료 모음

### 1. CI/CD와 Github Action 기본 개념을 배우고 FastAPI 애플리케이션 생성하기

- 1장 강의 숙제: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/homework1.yaml)

#### 1.1 CI/CD의 기본 개념과 필요성 학습

- 별도 실행한 Action YAML 또는 자료 링크 없음.

#### 1.2 GitHub Actions의 구조와 구성 요소 이해

- Hello World Yaml 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/hello_world.yaml)

- Hello World Action 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/hello_world.yaml)

- Linux CMD Yaml (Linux Command Practice) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/linux_cmd.yaml)

- Linux CMD Action (Linux Command Practice) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/linux_cmd.yaml)

- Hello Python Yaml (Simple Python Print Workflow) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/hello_python.yaml)

- Hello Python Action (Simple Python Print Workflow) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/hello_python.yaml)

- Hello Python `hello_world.py` 파일 (Simple Python Print Workflow) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/blob/main/01-tutorial/hello_world.py)

#### 1.3 FastAPI 애플리케이션 생성 및 기본 CI 설정

- 강의 전체 파이썬 의존성 `requirements.txt` 확인: [링크](./requirements.txt)

- 강의에서 사용하는 `FastAPI main.py` 확인: [링크](./02-fastapi/main.py)

- Fast API Yaml (Fast API with Github Action) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/fast_api.yaml)

- Fast API Action (Fast API with Github Action) 확인하기 : [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/fast_api.yaml)

### 2. Docker 이미지로 패키징된 애플리케이션과 Docker 빌드 자동화 워크플로우

- 2장 강의 숙제: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/homework2.yaml)

#### 2.1 리눅스 기본 & Docker의 기본 개념과 사용법 학습

- 학습한 리눅스 커맨드 정리: [링크](./03-linux-cmd/Readme.md)

- 리눅스 커맨드 쉘스크립트: [링크](./03-linux-cmd/linux_cmd.sh)

#### 2.2 애플리케이션의 Docker 이미지 생성, 그리고 멀티 스테이지 빌드를 통한 이미지 최적화

- Dockerfile : [링크](./Dockerfile)

#### 2.3 GitHub Actions로 Docker 빌드 자동화

- fastapi_docker_cicd YAML (Docker CI/CD) : [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/fastapi_docker_cicd.yaml)

- fastapi_docker_cicd Action (Docker CI/CD) : [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/fastapi_docker_cicd.yaml)

- Docker Build Cache 확인하기: [링크](https://github.com/RyanKor/devops-sparta/actions/caches)

### 3. 자동화된 테스트가 포함된 CI 파이프라인과 테스트 커버리지 리포트

- 3장 강의 숙제: [링크](https://github.com/RyanKor/sparta-action-builder)

#### 3.1 Pytest 작성, 그리고 코드 커버리지 설정하기

- pytest 실행을 위한 fastapi main.py: [링크](./04-test-fastapi/main.py)

- pytest 실행을 위한 test_main.py: [링크](./04-test-fastapi/test_main.py)

#### 3.2 GitHub Actions에서 테스트 자동화

- Pytest를 실행하는 Dockerfile: [링크](./04-test-fastapi/Dockerfile)

- 메타 데이터 추출 YAML: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/metadata.yaml)

- 메타 데이터 추출 Action: [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/metadata.yaml)

- Workflow Run 실행을 위한 첫번째 파이프라인 YAML: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/first_coverage_pipeline.yaml)

- Workflow Run 실행을 위한 첫번째 파이프라인 (First Coverage Pipeline): [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/first_coverage_pipeline.yaml)

- Workflow Run 실행을 위한 두번째 파이프라인 YAML: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/second_build_pipeline.yaml)

- Workflow Run 실행을 위한 두번째 파이프라인 (Second Build Pipeline): [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/second_build_pipeline.yaml)

#### 3.3 테스트 결과 분석 및 개선

- Docker Custom Action 분리하기: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/actions/custom-docker-build/action.yaml)

- Docker Custom Action YAML (도커 커스텀 필드 액션): [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/custom_action_docker_build.yaml)

- Docker Custom Action (도커 커스텀 필드 액션): [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/custom_action_docker_build.yaml)

- Workflow 스케줄링 YAML (Nightly Build and Test): [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/night_build_test.yaml)

- Workflow 스케줄링 Action (Nightly Build and Test): [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/night_build_test.yaml)

### 4. 자동 배포까지 완성된 CI/CD 파이프라인과 기본적인 모니터링이 적용된 배포 환경 구성하기

- 4장 강의 숙제: [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/homework4.yaml)

#### 4.1 배포 환경 구성

- 강의에 사용한 aws cli 및 IAM 설정 모음: [링크](./05-aws/Readme.md)

#### 4.2 GitHub Actions 추가 기능과 환경 관리

- Github Action -> EC2 SSH 접속 시, Docker 설치 안될 때 사용하는 수동 스크립트: [링크](./05-aws/install_docker.sh)

- 전체 CICD 파이프라인 YAML (Build, Push Docker Image and Deploy to AWS EC2): [링크](https://github.com/RyanKor/devops-sparta/blob/main/.github/workflows/aws_cicd_final.yaml)

- 전체 CICD 파이프라인 Action (Build, Push Docker Image and Deploy to AWS EC2): [링크](https://github.com/RyanKor/devops-sparta/actions/workflows/aws_cicd_final.yaml)

#### 4.3 모니터링 설정 및 배포 전략 수립

- 강의 전체 Action 목록: [링크](https://github.com/RyanKor/devops-sparta/actions)

- 디버깅 모드 Action 실행: [링크](https://github.com/RyanKor/devops-sparta/actions/runs/12494154293)

- Test, Docker build, AWS Deploy CI/CD 상태 체크 (Action Badge)

    - [![Build, Push Docker Image and Deploy to AWS EC2](https://github.com/RyanKor/devops-sparta/actions/workflows/aws_cicd_final.yaml/badge.svg)](https://github.com/RyanKor/devops-sparta/actions/workflows/aws_cicd_final.yaml)

- 트러블 슈팅 구성 예제: [링크](./06-troubleshooting/Readme.md)


