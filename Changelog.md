# Changelog

## [Unreleased]

### Ajouts
- Ajout du module `organizations` dans `app/modules/organizations`.
- Ajout des routes de lecture, creation et mise a jour des organisations.
- Ajout des schemas Pydantic pour les reponses et les payloads.
- Ajout du repository `organizations/repositories/main.py` pour la logique d'acces aux donnees.
- Ajout de l'autoloading centralise via `app/lib/autoloader.py`.
- Ajout de la documentation d'architecture et des guides de developpement dans `docs/`.

### Modifications
- Mise a jour de la structure du projet pour separer la logique partagée (`app/lib`) des modules metier (`app/modules`).
- Alignement du README sur la structure réelle de l'application et les modules implementes.
- Centralisation des parametres SQLAlchemy et de la session dans `app/lib/sql.py`.

### Suppressions
- Suppression des anciennes structures obsoletes de l'ancien modele de projet.
- Nettoyage des anciens fichiers de configuration et de documentation redondants.
