from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

#Request all the blogs
@router.get("/blog", response_model = List[schemas.ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all() 
    return blogs

#Creating a new entry in our blog table in the database
@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, database_instance: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    database_instance.add(new_blog)
    database_instance.commit()
    database_instance.refresh(new_blog)
    return new_blog

#Delete a blog
@router.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id, database_instance: Session = Depends(get_db)):
    blog = database_instance.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = 404, detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    database_instance.commit()
    return 'Blog is deleted successfuly'

#Update a blog
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def updated(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not found')
    blog.update(request.model_dump())
    db.commit()
    return 'updated successfuly'

#Show a single blog
#Response will be the same as the ShowBlog schema(Just the title)
@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id ,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    #Create server response with status code of 404, for bad requests.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = 
                            f'Blog with the id {id} is not available.')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'Blog with the id {id} is not available.'}
    return blog
