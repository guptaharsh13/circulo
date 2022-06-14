import os
from django.core.asgi import get_asgi_application
import environ
from pathlib import Path

path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      f'circulo.settings.{env("django_env")}')

application = get_asgi_application()
