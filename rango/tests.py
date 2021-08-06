from django.test import TestCase
from rango.views import category_add_like, recipe_add_like, if_category_exist, add_recipes_to_dict
from rango.models import Category, Recipe, FavouriteRecipe, UserProfile
from django.contrib.auth.models import User
from populate_rango import populate
import json
import os

# Create your tests here.


class CategoryMethodTests(TestCase):
    def add_like(self):
        category = Category.objects.get(id=1)
        old_likes = category.likes
        category_add_like(category.slug)

        self.assertEqual(old_likes, category.likes)


class RecipeMethodTests(TestCase):
    def add_likes(self):
        recipe = Recipe.objects.get(id=1)
        old_likes = recipe.likes
        recipe_add_like(recipe.id)

        self.assertEqual(old_likes, recipe.likes)

#
# class FavouriteRecipe(TestCase):
#     # def setUp(self):
#     #     populate()
#
#     def test_favourite_recipe(self):
#         user = User.objects.get(username="fan")
#         user_profile = UserProfile.objects.get(id=user)
#         favourite_recipe = FavouriteRecipe.objects.get(user=user_profile)
#         recipes = Recipe.objects.filter(favouriteRecipe=favourite_recipe)
#         fc = add_recipes_to_dict(recipes)
#
#         recipes_dict = [
#             {
#                 'recipeId': 10,
#                 'recipeSlug': "strawberry-rhubarb-buckle",
#                 'recipeTitle': "Strawberry-Rhubarb Buckle",
#             }
#         ]
#         context_dict = {
#             'success': True,
#             'data': {
#                 'recipes': recipes_dict,
#             }
#         }
#
#         self.assertEqual(context_dict, fc)
