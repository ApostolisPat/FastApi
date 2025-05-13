from fastapi import FastAPI

app = FastAPI() #Call object

#Decorate with @
@app.get('/')
def index():
    return {"data": {"name":"Apostolis"}}

@app.get('/about')
def about():
    return {"data": "about page"}