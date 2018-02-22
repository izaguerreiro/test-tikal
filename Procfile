web: gunicorn tikal.wsgi --log-file -
worker: celery --app=tikal worker --beat --loglevel=info