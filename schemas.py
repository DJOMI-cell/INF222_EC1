from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ArticleBase(BaseModel):
    titre: str
    contenu: str
    auteur: str
    categorie: Optional[str] = None
    tags: Optional[str] = None

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    date_creation: datetime

    class Config:
        from_attributes = True