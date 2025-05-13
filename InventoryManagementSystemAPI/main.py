from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  #initializes an object(FastAPI object)

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you'd like to view.",gt = 0)): #Type int in Python is "variable_name: type"
    return inventory[item_id]

#Query parameters
# facebook.com/home?key=15
#get-by-name endpoint requires a query parameter like get-by-name?name=Milk
# http://127.0.0.1:8000/get-by-name?test=2&name=Milk
@app.get("/get-by-name")
def get_item(name: str): #=None is default value
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail = "Item name not found.")

#Requst Body
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail = "Item ID already exists.")
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail = "Item ID does not exist.")
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt = 0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail = "Item ID does not exist.")
    
    del inventory[item_id]
    return{"Success": "Item deleted!"}

