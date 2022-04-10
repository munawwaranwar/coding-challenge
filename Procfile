release: python manage.py migrate
web: waitress-serve --port=$PORT documents_store.wsgi:application