from django_seed import Seed
from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help = "How many users do you wnat you create?"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser':False
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))

