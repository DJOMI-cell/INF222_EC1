# 📘 API Blog avec FastAPI et MySQL

 DESCRIPTION 

Ce projet consiste en la réalisation d’une API REST pour la gestion d’articles de blog en utilisant **FastAPI**, **SQLAlchemy** et une base de données **MySQL**.

L’API permet d’effectuer les opérations CRUD (Create, Read, Update, Delete) sur les articles.



 TECHNOLOGIES UTILISÉES 

* Python 3.11+
* FastAPI
* Uvicorn
* SQLAlchemy
* MySQL
* Pydantic



STRUCTURE du PROJET 


BlogAPI/
│── main.py          # Point d’entrée de l’application
│── models.py        # Modèles SQLAlchemy
│── schemas.py       # Schémas Pydantic
│── crud.py          # Logique CRUD
│── database.py      # Configuration de la base de données
│── env/             # Environnement virtuel




INSTALLATION et CONFIGURATION 

Cloner le projet

bash
git clone <url_du_projet>
cd BlogAPI




 Créer un Environnement virtuel

bash
python -m venv env


Activer :

bash
.\env\Scripts\activate



INSTALLÉE les DÉPENDANCES 

bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python




CONFIGURATION de la BASE de DONNÉES 

Dans `database.py` :

**python
DATABASE_URL = "mysql+mysqlconnector://root:motdepasse@localhost/blog_api"


NB:Remplace `motdepasse` par ton vrai mot de passe MySQL.


CRÉER la BASSE de DONNÉES 

Dans MySQL :

sql
CREATE DATABASE blog_api;



LANCÉE le SERVEUR :

bash
uvicorn main:app --reload



ACCÈS à l’API

* API : http://127.0.0.1:8000
* Documentation Swagger : http://127.0.0.1:8000/docs



 END POINTS DISPONIBLES :
 
 Créer un article

POST /api/articles


Exemple :

  __json
{
  "titre": "Mon article",
  "contenu": "Contenu de l'article",
  "auteur": "Steph",
  "categorie": "Tech",
  "tags": "python"
}




Lire tous les articles


GET /api/articles


 Lire un article


GET /api/articles/{id}


Modifier un article


PUT /api/articles/{id}


Supprimer un article


DELETE /api/articles/{id}



FONCTIONNALITÉS IMPLÉMENTÉES 

* Création d’articles
* Récupération de tous les articles
* Récupération par ID
* Mise à jour d’un article
* Suppression d’un article
* Connexion à une base MySQL
* Gestion des erreurs (404, doublons, etc.)



GESTION des ERREURS 

* 404 : Article non trouvé
* 400 : Doublon de titre (si activé)
* 500 : Erreur interne serveur



EXEMPLE avec cURL

bash
curl -X POST http://127.0.0.1:8000/api/articles \
-H "Content-Type: application/json" \
-d '{
  "titre": "Test",
  "contenu": "Contenu test",
  "auteur": "Steph"
}'




RÉINITIALISATION de la BASE 

Pour vider la table :

sql
TRUNCATE TABLE articles;




AUTEUR

Projet réalisé par : Stéphane Djomi

CONCLUSION :

Ce projet démontre la mise en place d’une API REST complète avec FastAPI et MySQL, respectant les bonnes pratiques de développement backend.

