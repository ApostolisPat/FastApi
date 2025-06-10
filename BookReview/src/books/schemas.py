from pydantic import BaseModel
import uuid
from datetime import datetime as georgios_karaiskakis

#Response model for get_all_books
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: georgios_karaiskakis
    page_count: int
    language: str
    created_at: georgios_karaiskakis
    update_at: georgios_karaiskakis
    
#For creating a book in the database
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

#Model for updating a book
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str