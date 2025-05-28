from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash



app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creating a new entry in our blog table in the database
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, database_instance: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    database_instance.add(new_blog)
    database_instance.commit()
    database_instance.refresh(new_blog)
    return new_blog

#Delete a blog
@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id, database_instance: Session = Depends(get_db)):
    blog = database_instance.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = 404, detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    database_instance.commit()
    return 'Blog is deleted successfuly'
    
#Update a blog
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def updated(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not found')
    blog.update(request.model_dump())
    db.commit()
    return 'updated successfuly'
    

#Request all the blogs
@app.get("/blog", response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all() 
    return blogs

#Show a single blog
#Response will be the same as the ShowBlog schema(Just the title)
@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response ,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    #Create server response with status code of 404, for bad requests.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = 
                            f'Blog with the id {id} is not available.')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'Blog with the id {id} is not available.'}
    return blog




#Create new user
@app.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = 
                    f'User with the id {id} is not available.')
        
    return user