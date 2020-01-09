import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
django.setup()

import random
from .models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'News']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
         top = add_topic()
         fake_url = fakegen.url()
         fake_name = fakegen.name()
         fake_date =fakegen.date()

         webpg = Webpage.objects.get_or_create(topics=top, url=fake_url, name=fake_name)[0]
         acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("populate Script")
    populate(8)
    print("populate complete")





