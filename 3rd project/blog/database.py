from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a base
Base = declarative_base()