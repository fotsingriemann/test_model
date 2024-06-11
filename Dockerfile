# Utiliser l'image Python officielle en tant qu'image de base
FROM python:3.9

# Définir le répertoire de travail dans l'image Docker
WORKDIR /usr/src/app

# Copier le fichier requirements.txt dans le répertoire de travail de l'image Docker
COPY requirements.txt ./

# Installer les dépendances Python spécifiées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le répertoire de travail de l'image Docker
COPY . .

# Exposer le port sur lequel l'application Django s'exécutera
EXPOSE 8000

# Commande pour démarrer l'application Django lorsque le conteneur Docker est lancé
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]

