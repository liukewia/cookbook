from rango.models import Category, Recipe, FavouriteRecipe, UserProfile, User
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()


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
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5968118.jpg&w=958&h=1274&c=sc&poi=face&q=85',
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
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F8711239.jpg&q=85',
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
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4537394.jpg&w=958&h=958&c=sc&poi=face&q=85',
         'likes': 23}]

    Bread_recipes = [
        {'title': 'Strawberry Bread',
         'ingredients': """
2 cups fresh strawberries
3 cups all-purpose flour
2 cups white sugar
1 tablespoon ground cinnamon
1 teaspoon salt
1 teaspoon baking soda
1.25 cups vegetable oil
4 eggs, beaten
1.25 cups chopped pecans
         """,
         'directions': """
        Preheat oven to 350 degrees F (175 degrees C). Butter and flour two 9 x 5-inch loaf pans.
        Slice strawberries and place in medium-sized bowl. Sprinkle lightly with sugar, and set aside while preparing batter.
        Combine flour, sugar, cinnamon, salt and baking soda in large bowl; mix well. Blend oil and eggs into strawberries. Add strawberry mixture to flour mixture, blending until dry ingredients are just moistened. Stir in pecans. Divide batter into pans.
        Bake in preheated oven until a tester inserted in the center comes out clean, 45 to 50 minutes (test each loaf separately). Let cool in pans on wire rack for 10 minutes. Turn loaves out of pans, and allow to cool before slicing.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5470594.jpg&w=767&h=767&c=sc&poi=face&q=85',
         'likes': 30},
        {'title': 'Whole Wheat Beer Bread ',
         'ingredients': """1/2 cups all-purpose flour
1/2 cups whole wheat flour
1/2 teaspoons baking powder
1/2 teaspoons salt
1/3 cup packed brown sugar
1 (12 fluid ounce) can or bottle beer
""",
         'directions': """Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9x5 inch loaf pan.
In a large mixing bowl, combine all-purpose flour, whole wheat flour, baking powder, salt and brown sugar. Pour in beer, stir until a stiff batter is formed. It may be necessary to mix dough with your hands. Scrape dough into prepared loaf pan.
Bake in preheated oven for 50 to 60 minutes, until a toothpick inserted into center of the loaf comes out clean.
""",
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F128314.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 26},
        {'title': 'Garlic Naan',
         'ingredients': """
        1/2 cup warm water
        1 teaspoon white sugar
        1 (.25 ounce) package active dry yeast
        For the Garlic Butter:
        1/4 cup butter
        2 cloves garlic, minced
        1/4 cup plain yogurt
        2 cups bread flour, or more as needed
        1 teaspoon kosher salt
        1/4 cup chopped cilantro (Optional)
         """,
         'directions': """
        Combine water, sugar, and yeast in a bowl. Let stand until yeast softens and forms a creamy foam, about 15 minutes.
        In the meantime, heat butter in a pan over medium heat until melted and sizzling. Quickly mix in garlic. Remove garlic butter from heat and set aside until ready to use.
        Add yogurt, bread flour, salt, and 1 tablespoon of the garlic butter to the yeast mixture. Stir with a wooden spoon until a shaggy dough forms. Knead by hand until dough pulls away from the sides of the bowl, adding more water or flour as needed. Turn dough out onto the counter and continue kneading into a smooth ball, 3 to 4 minutes.
        Place dough in a large bowl. Coat with a few more drizzles of garlic butter. Cover and let rise until doubled in volume, about 2 hours.
        Punch down dough and turn out onto the counter. Shape into a rough rectangle and cut into 6 pieces. Roll each piece into a ball and lightly dust with flour. Cover with plastic wrap and proof until slightly puffy, 15 to 20 minutes.
        Roll each piece into an oval about 1/8 inch thick. Sprinkle some cilantro on top and press lightly to adhere.
        Preheat a cast iron skillet until very, very hot, about 5 minutes. Cook each naan until large bubbles form, 1 to 2 minutes. Flip over, press gently, and cook until bubbles on the bottom are charred, 2 to 3 minutes more.
        Brush naan with more garlic butter before serving.
         """,
         'url': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6599025.jpg&w=1200&h=678&c=sc&poi=face&q=85',
         'likes': 23}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'likes': 20},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'likes': 50},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'likes': 18}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'likes': 15},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'likes': 10}]

    cats = {'BBQ': {'recipes': BBQ_recipes,  'likes': 64},
            # 'Bread': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Breakfast and Brunch': {'recipes': BBQ_recipes,  'likes': 16},
            # 'Desserts': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Dinner': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Everyday Cooking': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Lunch': {'recipes': BBQ_recipes, 'likes': 32},
            # 'Main Dishes': {'recipes': BBQ_recipes, 'likes': 32},
            }

    # favs = {'user': 'mockusername', 'recipe': 'Best Steak Marinade in Existence'}

    # for cat, cat_data in cats.items():
    #     c = add_cat(cat, likes=cat_data['likes'])
    #     for r in cat_data['recipes']:
    #         add_recipe(c, r['title'], r['ingredients'], r['directions'], r['url'], likes=r['likes'])
    #
    # for c in Category.objects.all():
    #     for r in Recipe.objects.filter(category=c):
    #         print(f'- {c}: {r}')

    # add_user_profile()
    create_favourite_recipe()

    # add_to_favourite_recipe(favs['user'], favs['title'])


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


# def add_user_profile():
#     user = User.objects.get(id=1)
#     up = UserProfile.objects.create(user=user)
#     up.save()

def create_favourite_recipe():
    user = User.objects.get(id=1)
    user_profile = UserProfile.objects.get(user=user)
    favourite_recipe = FavouriteRecipe.objects.get_or_create(user=user_profile)[
        0]
    recipe = Recipe.objects.get(id=12)
    recipe.favouriteRecipe.add(favourite_recipe)


# def add_to_favourite_recipe(username, title):
#     r = Recipe.objects.get_or_create(title=title)[0]
#     u = User.objects.get_or_create(username=username)[0]
#     up = UserProfile.objects.get_or_create(user=u)[0]
#     f = FavouriteRecipe.objects.get_or_create(user=up)[0]
#     r.favouriteRecipe = f
#
#     return f


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
