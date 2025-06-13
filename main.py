from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model for the product
class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

fake_db = {}

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    if product.name in fake_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    fake_db[product.name] = product
    return product

@app.get("/products/{name}", response_model=Product)
def read_product(name: str):
    product = fake_db.get(name)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{name}", response_model=Product)
def update_product(name: str, updated: Product):
    if name not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    fake_db[name] = updated
    return updated

@app.patch("/products/{name}", response_model=Product)
def patch_product(name: str, partial: Product):
    if name not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    existing = fake_db[name]
    update_data = partial.dict(exclude_unset=True)
    updated = existing.copy(update=update_data)
    fake_db[name] = updated
    return updated

@app.delete("/products/{name}")
def delete_product(name: str):
    if name not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del fake_db[name]
    return {"message": f"Deleted product '{name}' successfully"}
