from django.test import TestCase, Client

from rango.models import Category, Recipe
from rango.views import category_add_like, recipe_add_like


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


class PageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)


class BingApiTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_bing_search(self):
        response = self.client.get('/api/bing_search?q=recipe')
        self.assertTrue(response.status_code, 200)
