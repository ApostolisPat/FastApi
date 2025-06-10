# Service.py will serve CRUD methods with our database
# Means that when the path function (e.g. get_all_books) is run, the get_all_books from the service
# will also run, to retrieve all the books from the database

from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .models import Book
from datetime import datetime

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at)) #Select the book model in the *database* and order by descending order
        
        result = await session.exec(statement) #Wait for execution
        
        return result.all() #Return all results
         
            
    async def get_book(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        
        result = await session.exec(statement)
        
        book = result.first()
        
        return book if book is not None else None
            
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        
        #Creates a new Book object in the db, that contains the attribute from the book_data_dict
        new_book = Book(
            **book_data_dict
        )
        
        new_book.published_date = datetime.strptime(book_data_dict['published_date'],"%Y-%m-%d")
        
        session.add(new_book) # Add operation in the database
        
        await session.commit() #Commit to the database
        
        return new_book
    
    async def update_books(self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession):
        book_to_update = await self.get_book(book_uid, session) #use the get_book function to retrieve the book from db

        if book_to_update is not None:
            update_data_dict = update_data.model_dump()
            
            #for each key and value in dicitonary...
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
                
            await session.commit()
            
            return book_to_update
        else:
            return None
      
    
    async def delete_books(self, book_uid: str, session: AsyncSession):
        book_to_delete = await self.get_book(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            
            await session.commit()
            
            return {}
            
        else:
            return None