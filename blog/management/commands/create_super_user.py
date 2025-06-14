# blog/management/commands/create_superuser_from_env.py
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# This is the main class for our command
class Command(BaseCommand):
    # A short description of the command, which will show up in 'manage.py help'
    help = "Creates a superuser from environment variables (DJANGO_SUPERUSER_USERNAME, etc.)"

    # This is the main logic of the command
    def handle(self, *args, **options):
        # We get the credentials from the environment variables
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        # We check if a user with that username already exists
        if not User.objects.filter(username=username).exists():
            # If the user does not exist, we create them.
            self.stdout.write(f'Creating account for {username}')
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            # If the user already exists, we print a message and do nothing.
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
