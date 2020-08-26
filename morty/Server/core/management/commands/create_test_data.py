from django.core.management.base import BaseCommand, CommandError

from core.models import ImageData

class Command(BaseCommand):
    """Creates test data""" 
    def handle(self, *args, **options):
        data = (
            ('Title Card', 'rm1.jpg'),
            ('Old Title', 'rm2.jpg'),
            ('Field', 'rm3.jpg'),
            ('Saturn', 'rm4.jpg'),
            ('Portal', 'rm5.jpg'),
            ('Pickle Rick', 'rm6.jpg'),
            ('Spock', 'rm7.jpg'),
            ('Angry', 'rm8.jpg'),
            ('Meta', 'rm9.jpg'),
            ('Family Trip', 'rm10.jpg'),
        )

        for name, filename in data:
            ImageData.objects.create(name=name, filename=filename)
