#This reads from the .env file

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    DATABASE_URL: str = "" #Get the variable DATABASE_URL from the .env file, default to empty string
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )
    
Config = Settings()