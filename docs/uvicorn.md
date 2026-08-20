# Lancer l'API avec Uvicorn

## Prerequis

Activer l'environnement virtuel et installer les dependances en suivant le
guide [Environnement de developpement](environnement.md).

## Demarrer le serveur

Depuis la racine du projet :

```powershell
uvicorn main:app --reload
```

- `main` correspond au fichier `main.py`.
- `app` correspond a l'instance FastAPI exposee par `main.py`.
- `--reload` redemarre le serveur lorsqu'un fichier est modifie. Cette option
  est reservee au developpement.

L'API est accessible par defaut a l'adresse suivante :

```text
http://127.0.0.1:8000
```

La documentation interactive est disponible sur :

- Swagger UI : `http://127.0.0.1:8000/docs`
- ReDoc : `http://127.0.0.1:8000/redoc`

## Arreter le serveur

Dans le terminal qui execute Uvicorn, utiliser `Ctrl+C`.
