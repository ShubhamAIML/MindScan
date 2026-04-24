release: python manage.py collectstatic --no-input --clear
web: gunicorn mental_health_app.wsgi:application --bind 0.0.0.0:$PORT
