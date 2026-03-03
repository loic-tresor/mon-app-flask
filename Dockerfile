FROM python:3.11-slim

# Création de l'utilisateur sécurisé [cite: 59, 108]
RUN useradd -m loicuser
USER loicuser
WORKDIR /home/loicuser

# Installation des dépendances [cite: 60]
COPY --chown=loicuser:loicuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source [cite: 146]
COPY --chown=loicuser:loicuser app/ ./app/

EXPOSE 5000
CMD ["python", "app/app.py"]