from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI() #Create an instance of FastAPI object

# ('/')  = path
# .get   = operation
# @app   = path operation decorator
# def    = path operation function
@app.get('/')
def index():
    return {"data": 'Home'}

# Query parameter (limit,published)
# you have to do validation on the query parameter
@app.get('/blog')
def blogs(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}

# This path needs to be moved before /blog/{id}
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

# Before using the id variable from the path, you have to accept it as the functions parameter
@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}



@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    #fetch comments of blog with id=id
    return {"data": {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool] = False

#Post method
@app.post('/blog')
def create_blog(requestBody: Blog):
    return {'data':f'Blog is created with title: {requestBody.title}'}

#run uvicorn through main
""" if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000) """