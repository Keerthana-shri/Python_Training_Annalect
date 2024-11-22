from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from PS1_logic import Logic

# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    productid: int
    productname: str
    price: float

# Initialize FastAPI app
app = FastAPI()

@app.post("/addproduct")
async def add_product(new_product: Product):
    print("inside add", new_product)
    return True

@app.put("/updateproduct/{productid}")
async def update_product(updated_product: Product):
    print("inside update", updated_product)
    return True

@app.get("/listproducts")
async def list_products():
    products = [4, "Pen", 30]
    return products

@app.put("/applydiscount/{productid}")
async def apply_discount(productid: int, discount: float):
    print(f"Applying discount of {discount}% to product with ID {productid}")
    return {"productid": productid, "discount_applied": discount}

