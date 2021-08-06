import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from django.test import TestCase
from rango.views import category_add_like, show_category
from rango.models import Category


# Create your tests here.

# add_to_favourite_recipe
# add_recipes_to_dict
# if_category_exist
# recipe_add_like

# class CategoryMethodTests(TestCase):
#     def add_like(self):
#         category = Category.objects.get(id=1)
#         old_likes = category.likes
#         category_add_like(category.slug)
#
#         self.assertEqual(old_likes, category.likes)
#


