#This files contains the database models for each entity

import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field, Column
from datetime import date, datetime

#this will be a table named books
class Book(SQLModel, table=True):
    __tablename__ = "books" #Define the table name
    
    #id for postgresql
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, default=datetime.now))
    
    def __repr__(self):
        return f"<Book {self.title}>"
