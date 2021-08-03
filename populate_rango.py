import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Recipe


def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'likes': 30},
        {'title': 'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'likes': 26},
        {'title': 'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'likes': 23} ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'likes': 20},
        {'title': 'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'likes': 50},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'likes': 18} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'likes': 15},
        {'title': 'Flask',
         'url':'http://flask.pocoo.org',
         'likes': 10} ]

    cats = {'Python': {'pages': python_pages,  'likes': 64},
             'Django': {'pages': django_pages, 'likes': 32},
             'Other Frameworks': {'pages': other_pages,  'likes': 16} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], likes=p['likes'])

    for c in Category.objects.all():
        for p in Recipe.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, likes=0):
    p = Recipe.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.likes=likes
    p.save()
    return p


def add_cat(name, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.save()
    return c


if __name__=='__main__':
    print('Starting Rango population script...')
    populate()


