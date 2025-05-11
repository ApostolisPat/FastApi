from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

#API: Application Programming Interface

#go to 127.0.0.1:8000/docs to see interactive documentation
#or
#127.0.0.1:8000/redoc


class Item(BaseModel):
    text: str #required value because it doesn't have a default value
    is_done: bool = False

items = [] # Todo items

@app.get("/") #Root directory. When someone visits '/', this function is going to be called
def root():
    return {"Hello": "World"}

#Call this with this:
#curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple' on gitbash
#When we create the Item class, the above command won't work. Use:
#curl -X POST -H "Content-Type: application/json" -d '{"text": "apple"}' 'http://127.0.0.1:8000/items'
@app.post("/items") #New endpoint for our app. Users can access by sending an HTTP Post request
def create_item(item: Item):
    items.append(item)
    return items

#Call this with this:
#curl -X GET 'http://127.0.0.1:8000/items?limit=3'
#or
##curl -X GET 'http://127.0.0.1:8000/items'
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

#Call this with this:
#curl -X GET http://127.0.0.1:8000/items/0
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items): #Error handling when item doesn't exist 
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found") #Raise 404 exception