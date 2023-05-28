from django.core.management.base import BaseCommand

from ...models import Passenger

import pandas as pd

class Command(BaseCommand):
    help = 'Import bite exercise stats'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--csv_path', required=True)

    def handle(self, *args, **options):
        print(options)
        file_path = options["csv_path"]

        df = pd.read_csv(file_path)

        for idx, row in df.iterrows():
            stat, created = Passenger.objects.get_or_create(
                name=row['Name'],
                sex=row['Sex'],
                survived=row['Survived'],
                age=row['Age'],
                ticket_class=row['Pclass'],
                embarked=row['Embarked'],
            )

            if created:
                self.stdout.write(f"{stat} created")
            else:
                self.stderr.write(f"{stat} already in db")