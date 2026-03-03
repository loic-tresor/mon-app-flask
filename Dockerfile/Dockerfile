# 1. Image de base légère (Python 3.11 sur Alpine Linux)
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code de l'application
COPY . .

# 6. Exposer le port utilisé par Flask
EXPOSE 5000

# 7. Commande pour lancer l'application
CMD ["python", "app.py"]