from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

#To connect to db. Open psql(if using postgresql)
#run \c bookreview_db

#create an async engine
async_engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True
    )
)

#Function to create a connection to the database
async def init_db():
    async with async_engine.begin() as conn:
        #Create the database tables
        from src.books.models import Book #Import db models
        
        #This line searches for all models that extend the SQLModel object and creates them
        await conn.run_sync(SQLModel.metadata.create_all)
        
#Function create a session for our database connection
async def get_session()->AsyncSession:
    
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False 
    )
    
    async with Session() as session:
        yield session