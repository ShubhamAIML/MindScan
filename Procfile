release: python manage.py collectstatic --noinput --clear --verbosity 2
web: gunicorn mental_health_app.wsgi:application --bind 0.0.0.0:$PORT --workers 1
