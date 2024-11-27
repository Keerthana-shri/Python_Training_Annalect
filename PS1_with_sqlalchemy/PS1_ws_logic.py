from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from PS1_logic import Logic

app = FastAPI()
logic = Logic()

class Product(BaseModel):
    productid: int
    productname: str
    price: float

@app.post("/add_product", status_code=status.HTTP_201_CREATED)
async def add_product(new_product: Product):
    result = logic.add_product(new_product)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Addition of product failed"
        )
    return result

@app.get("/get_products", status_code=status.HTTP_200_OK)
async def get_product():
    result = logic.list_all()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found"
        )
    return result

@app.put("/update_product", status_code=status.HTTP_200_OK)
async def update_product(update_product: Product):
    result = logic.update_product(update_product)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return result

@app.put("/apply_discount", status_code=status.HTTP_200_OK)
async def apply_discount(discount_percentage: int):
    result = logic.apply_discount(discount_percentage)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid discount percentage"
        )
    return result

