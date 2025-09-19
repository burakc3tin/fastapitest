from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool] = None

items = {
    1:{"name": "Cep Telefonu", "price": 10.99, "is_offer": False},
    2:{"name": "Kamera", "price": 19.99, "is_offer": True}
}

@app.get("/api/products/{product_id}")
async def read_product(product_id: int):
    if product_id not in items:
        raise HTTPException(status_code=404, detail="Product not found")
    return items[product_id]


@app.post("/api/products")
async def create_product(item: Item):
    new_id = len(items) +1
    items[new_id] = item.dict()
    return {"message": "Product created", "product_id": new_id}