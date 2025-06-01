from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog as blog_repository

router = APIRouter(
    #Define the prefix for this router
    prefix="/blog",
    #Define the tags for this router
    tags=['Blogs']
)

#Request all the blogs
@router.get("/", response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)

#Creating a new entry in our blog table in the database
@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request: schemas.Blog, database_instance: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.create(request, database_instance)
    

#Delete a blog
@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, database_instance: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.destroy(id, database_instance)

#Update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updated(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.update(id, request, db)

#Show a single blog
#Response will be the same as the ShowBlog schema(Just the title)
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int ,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.show(id, db)
