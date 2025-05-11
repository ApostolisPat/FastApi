from fastapi import FastAPI

app = FastAPI()  #initializes an object(FastAPI object)

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}