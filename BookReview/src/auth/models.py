from datetime import datetime
from sqlmodel import Column, Field, SQLModel
import sqlalchemy.dialects.postgresql as pg
import uuid

#Table for users
class User(SQLModel, table=True):
    __tablename__ = 'users'
    #id for postgresql
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    def __repr__(self):
        return f"<User {self.username}>"