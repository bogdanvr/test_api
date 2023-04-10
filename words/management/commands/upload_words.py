from django.core.management.base import BaseCommand
from testapi.settings import BASE_DIR
from words.models import Words
from users.models import User
import csv


class Command(BaseCommand):
    help = 'Upload words to base. To do this,' \
           ' you need to upload a file "words.csv" to the root directory of the site.'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='Indicates the id of user whose words to be upload')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        user = User.objects.get(id=user_id)
        print(user)
        with open(f'{BASE_DIR}/words.csv') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                print('row', row)
                Words.objects.create(word=row[0], translate=row[1], user=user)
