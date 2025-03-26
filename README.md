### 1. Cloner le projet

```bash
git clone https://github.com/ElMonkito/V-Finance-Backend.git
```

### 2. Créer et activer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# ou
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la base PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'v_finance',
        'USER': 'mon_user',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Appliquer les migrations
```bash
python3 manage.py migrate
```

### 6. Créer un superuser
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```