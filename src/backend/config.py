import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    # DATABASE_URI = os.getenv("DATABASE_URI")


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_PORT", "8000"))


class ProductionConfig(Config):
    DEBUG = False
