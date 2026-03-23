from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL MySQL (utilise ta base existante)
DATABASE_URL = "mysql+mysqlconnector://root:IDiphone(2003)@localhost/blog_api"

# Création moteur
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base
Base = declarative_base()