from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **kwargs):
        email = 'admin@example.com'
        password = 'pass1234'

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{email}"'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{email}" already exists'))