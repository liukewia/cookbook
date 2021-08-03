import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Recipe


def populate():

    BBQ_recipes = [
        {'title': 'Best Steak Marinade in Existence',
         'ingredients': """1/3 cup soy sauce.
1/2 cup olive oil.
1/3 cup fresh lemon juice.
1/4cup Worcestershire sauce.
1.5 tablespoons garlic powder.
3 tablespoons dried basil.
1.5 tablespoons dried parsley flakes.
1 teaspoon ground white pepper.
1/4 teaspoon hot pepper sauce (Optional).
1 teaspoon dried minced garlic (Optional).
         """,
         'directions': """
         Place the soy sauce, olive oil, lemon juice, Worcestershire sauce, garlic powder, basil, parsley, and pepper in a blender. Add hot pepper sauce and garlic, if desired. 
         Blend on high speed for 30 seconds until thoroughly mixed.Pour marinade over desired type of meat. Cover, and refrigerate for up to 8 hours. Cook meat as desired.
         """,
         'url':'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5968118.jpg&w=958&h=1274&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Summer Grilled Cabbage',
         'ingredients': """1 large head cabbage, cored and cut into 8 wedges
8 teaspoons butter
1/4 cup water
1/2 teaspoon garlic powder, or to taste
1/2 teaspoon seasoned salt, or to taste
ground black pepper to taste
""",
         'directions': """Preheat an outdoor grill for medium-high heat and lightly oil grate.
Arrange the cabbage wedges into the bottom of a large metal baking dish. Pour the water into the dish. Place a teaspoon of butter on each cabbage wedge. Season liberally with garlic powder, seasoned salt, and pepper. Cover the dish with aluminum foil.
Place the dish on the preheated grill; cook until cabbage is tender, about 30 minutes.
""",
         'url':'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F8711239.jpg&q=85',
         'likes': 26},
        {'title': 'Grilled Salmon',
         'ingredients': """
         1.5 pounds salmon fillets
         lemon pepper to taste
         garlic powder to taste
         salt to taste
         1/3 cup soy sauce
         1/3 cup brown sugar
         1/3 cup water
         1/4 cup vegetable oil
         """,
         'directions': """
         Season salmon fillets with lemon pepper, garlic powder, and salt.
         In a small bowl, stir together soy sauce, brown sugar, water, and vegetable oil until sugar is dissolved. Place fish in a large resealable plastic bag with the soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours.
         Preheat grill for medium heat.
         Lightly oil grill grate. Place salmon on the preheated grill, and discard marinade. Cook salmon for 6 to 8 minutes per side, or until the fish flakes easily with a fork.
         """,
         'url':'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4537394.jpg&w=958&h=958&c=sc&poi=face&q=85',
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

    cats = {'BBQ': {'recipes': BBQ_recipes,  'likes': 64},
            # 'Bread': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Breakfast and Brunch': {'recipes': BBQ_recipes,  'likes': 16},
            # 'Desserts': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Dinner': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Everyday Cooking': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Lunch': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Main Dishes': {'recipes': BBQ_recipes, 'likes': 32},
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat, likes=cat_data['likes'])
        for r in cat_data['recipes']:
            add_recipe(c, r['title'], r['ingredients'], r['directions'], r['url'], likes=r['likes'])

    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            print(f'- {c}: {r}')


def add_recipe(cat, title, ingredients, directions, url, likes=0):
    r = Recipe.objects.get_or_create(category=cat, title=title)[0]
    r.ingredients = ingredients
    r.directions = directions
    r.url = url
    r.likes = likes
    r.save()
    return r


def add_cat(name, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.save()
    return c


if __name__=='__main__':
    print('Starting Rango population script...')
    populate()


