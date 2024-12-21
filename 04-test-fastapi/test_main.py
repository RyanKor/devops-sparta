import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def api_client():
    return client

# 시나리오 1: 기본 엔드포인트 정상 작동 확인
def test_read_root_success(api_client):
    response = api_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "Hello" in data
    assert data["Hello"] == "Sparta"

# 시나리오 2: 잘못된 요청 파라미터 처리 검증
# 목적: "/items"로 GET 요청 시 id 파라미터가 없으면 400 에러 반환
def test_items_no_id_param(api_client):
    response = api_client.get("/items")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Item ID is required"

# 시나리오 3: 응답 데이터 내용 및 형식 검증
# 목적: "/items"에 유효한 id를 전달하면 {"item_id": <int>, "name": <str>, "price": <int>} 구조의 데이터 반환
def test_items_valid_id(api_client):
    response = api_client.get("/items?id=123")
    assert response.status_code == 200
    data = response.json()
    # 응답 데이터 구조 검증
    assert "item_id" in data and isinstance(data["item_id"], int)
    assert "name" in data and isinstance(data["name"], str)
    assert "price" in data and isinstance(data["price"], int)
    # 값 검증
    assert data["item_id"] == 123
    assert data["name"] == "TestItem"
    assert data["price"] == 1000

# 시나리오 4: 성능/응답 시간 기본 검증 (단순히 응답 시간 측정)
# 목적: "/" 엔드포인트가 적절한 시간 내(예: 0.5초 이내)에 응답하는지 확인
# 범위: 단위 테스트(간단한 응답 시간 체크)
def test_response_time(api_client):
    import time
    start = time.time()
    response = api_client.get("/")
    end = time.time()
    assert response.status_code == 200
    assert (end - start) < 0.5, "응답 시간이 0.5초 이내여야 함"

# 시나리오 5: 키-값 타입 유효성 검증
# 목적: 응답 데이터 타입이 기대하는 Python 타입(dict, string)과 일치하는지 검증
# 범위: 단위 테스트
def test_response_value_type(api_client):
    response = api_client.get("/")
    data = response.json()
    assert isinstance(data, dict), "응답 데이터는 dict 형태여야 함"
    assert isinstance(data.get("Hello"), str), "'Hello' 키의 값은 문자열이어야 함"