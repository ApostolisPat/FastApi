from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all() 
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = 404, detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog is deleted successfuly'

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not found')
    blog.update(request.model_dump())
    db.commit()
    return 'updated successfuly'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    #Create server response with status code of 404, for bad requests.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = 
                            f'Blog with the id {id} is not available.')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'Blog with the id {id} is not available.'}
    return blog