from typing import Optional
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Sparta"}

# 새로운 기능: 특정 아이템을 조회하는 엔드포인트
# 시나리오 2, 3번을 위해 추가한 기능
# GET /items?id=123 와 같이 호출
# id 파라미터가 없거나 유효하지 않으면 400 에러 반환
@app.get("/items")
def read_item(id: Optional[int] = Query(None, description="Item ID")):
    if id is None:
        raise HTTPException(status_code=400, detail="Item ID is required")
    # 가상의 아이템 데이터
    return {"item_id": id, "name": "TestItem", "price": 1000}

@app.get("/dummy")
def read_dummy():
    return {"Hello": "Sparta"}