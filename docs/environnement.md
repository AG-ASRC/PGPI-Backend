# Environnement de developpement

## Creer l'environnement virtuel

Depuis la racine du projet :

```bash
python3 -m venv .venv
```

Sous Windows, la commande `python -m venv .venv` peut aussi etre utilisee si
`python3` n'est pas disponible.

## Activer l'environnement virtuel

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```bat
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Installer les dependances

Une fois l'environnement active :

```bash
pip install -r requirements.txt
```

Pour quitter l'environnement virtuel :

```bash
deactivate
```
