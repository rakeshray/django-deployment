import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django

# import settings
django.setup()

from AppTwo.models import AccessRecord, Topic, Webpage
from faker import Faker
import random

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_url = fakegen.url()

        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        acrecord = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
