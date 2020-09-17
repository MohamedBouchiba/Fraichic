release: python manage.py migrate --no-input
release: python manage.py makemigrations --no-input
web: gunicorn Fraichic.wsgi --log-file -
