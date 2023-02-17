from django.core.management.base import BaseCommand
from django.utils import timezone
import csv
from pathlib import Path


from reviews.models import Category, Genre, Title, Comment, Review
from users.models import User

PATH = "static/data/"

CSV_TABLE = {
    "category.csv": {"model": Category},
    "genre.csv": {"model": Genre},
    "titles.csv": {"model": Title},
    "users.csv": {"model": User},
    "review.csv": {"model": Review},
    "comments.csv": {"model": Comment},
    "genre_title.csv": {"m2m": {"model": Genre}}
}


class Command(BaseCommand):
    help = 'import data csv file to table on DB'

    def handle(self, *args, **kwargs):
        self.stdout.write(
            f"Импорт данных запущен: {timezone.now().strftime('%X')}")
        for import_file, data_for_save in CSV_TABLE.items():
            if 'model' in data_for_save.keys():
                data_for_save['model'].objects.all().delete()
                print(f"Данные модели {data_for_save['model']} удалены")
                with open(Path(PATH, import_file), encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    obj = [
                        data_for_save['model'](**dict(row)) for row in reader
                    ]
                    data_for_save['model'].objects.bulk_create(obj)
            if 'm2m' in data_for_save.keys():
                with open(Path(PATH, import_file), encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        data_for_save['m2m']['model'].objects.get(
                            id=row.get('genre_id')
                        ).titles.add(
                            row.get('title_id')
                        )
