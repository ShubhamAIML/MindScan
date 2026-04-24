import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health_app.settings')

application = get_wsgi_application()

# Wrap with WhiteNoise
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), '..', 'staticfiles'))
