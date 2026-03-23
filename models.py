from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255), nullable=False, unique=True)  # 🔒 pas de doublons sur le titre
    contenu = Column(Text, nullable=False)
    auteur = Column(String(100), nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow)
    categorie = Column(String(50))
    tags = Column(String(255))