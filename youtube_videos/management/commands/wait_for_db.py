import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
import os
import environ
from pathlib import Path

path = Path(__file__).resolve().parent.parent.parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        print("\n\n")
        print(env("db_password"))
        print("\n\n")
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
