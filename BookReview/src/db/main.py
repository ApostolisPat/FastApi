from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config


#To connect to db. Open psql(if using postgresql)
#run \c bookreview_db

#create an async engine
engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True
    )
)

#Function to create a connection to the database
async def init_db():
    async with engine.begin() as conn:
        #Create the database tables
        from src.books.models import Book #Import db models
        
        #This line searches for all models that extend the SQLModel object and creates them
        await conn.run_sync(SQLModel.metadata.create_all)
        