from database import engine

try:
    conn = engine.connect()
    print("Connexion à blog_api OK ✅")
except Exception as e:
    print("Erreur :", e)
finally:
    conn.close()