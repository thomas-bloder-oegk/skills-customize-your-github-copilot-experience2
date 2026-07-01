from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Student Items API")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float = Field(gt=0)


items = []
next_item_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Items API"}


@app.get("/health")
def read_health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Complete this route to return one item by ID.",
    )


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Complete this route to create and return a new item.",
    )