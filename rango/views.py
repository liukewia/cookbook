import json
from datetime import datetime

import requests
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.middleware import csrf
from django.shortcuts import render

from rango.models import Category, Recipe, FavouriteRecipe, Review, UserProfile


def index(request):
    return render(request, 'index.html')


def illegal_request_handler(request):
    return HttpResponse(status=404)


def get_all_categories(request):
    category_list = Category.objects.order_by('id')
    categories = []
    for category in category_list:
        category_dict = {
            'categoryName': category.name,
            'categorySlug': category.slug,
        }
        categories.append(category_dict)

    context_dict = {
        'success': True,
        'data': {
            'categories': categories
        }
    }

    return JsonResponse(context_dict)


def get_all_recipes(request):
    # get top10 most popular recipes
    recipe_list = Recipe.objects.order_by('-likes')[:10]
    recipes = []
    for recipe in recipe_list:
        recipe_dict = {
            'recipeId': recipe.id,
            'recipeTitle': recipe.title,
            'recipeDirection': recipe.directions,
            'recipePicture': recipe.url,
        }
        recipes.append(recipe_dict)

    context_dict = {
        'success': True,
        'data': {
            'recipes': recipes
        }
    }

    return JsonResponse(context_dict)


def add_recipes_to_dict(recipes):
    recipes_dict = []
    for recipe in recipes:
        recipe = {
            'recipeId': recipe.id,
            'recipeSlug': recipe.slug,
            'recipeTitle': recipe.title,
            'recipePic': recipe.url,
        }
        recipes_dict.append(recipe)

    context_dict = {
        'success': True,
        'data': {
            'recipes': recipes_dict,
        }
    }

    return context_dict


def show_category(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        recipes = None

    recipes_dict = []
    for recipe in recipes:
        recipe_dict = {
            'recipeId': recipe.id,
            'recipeTitle': recipe.title,
            'recipeDirection': recipe.directions[0:40],
            'recipeLike': recipe.likes,
            'recipeUrl': recipe.url,
        }
        recipes_dict.append(recipe_dict)

    context_dict = {
        'success': True,
        'data': {
            'categoryId': category.id,
            'categoryName': category.name,
            'categoryLikes': category.likes,
            'categorySlug': category.slug,
            'recipes': recipes_dict,
        }
    }

    return JsonResponse(context_dict)


@login_required
def add_category(request):
    cat_tuple = Category.objects.get_or_create(name=json.loads(request.body).get('name'))
    if cat_tuple[1]:
        context_dict = {
            'success': True,
            'data': {
                'status': 'ok'
            }
        }
    else:
        # if the category is already exists, return false
        context_dict = {
            'success': False,
            'data': {
                'message': 'The category already exists.'
            }
        }

    return JsonResponse(context_dict)


def if_category_exist(category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return False

    return True


@login_required
def category_add_like(request, category_name_slug):
    context_dict = {
        'success': True,
        'data': {}
    }
    if_exist = if_category_exist(category_name_slug)
    if not if_exist:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    category = Category.objects.get(slug=category_name_slug)
    likes = category.likes + 1
    category.likes = likes
    # save the object, otherwise the attribute will not change
    category.save()

    context_dict['data'] = {'likes': category.likes}

    return JsonResponse(context_dict)


def show_recipe(request, recipe_id):
    context_dict = {
        'success': True,
        'data': {}
    }

    try:
        recipe = Recipe.objects.get(id=recipe_id)
        reviews = Review.objects.filter(recipe=recipe)
    except Recipe.DoesNotExist:
        recipe = None
        reviews = None

    if recipe is None:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    # separate the string by \n
    ingredients = recipe.ingredients.split('\n')
    directions = recipe.directions.split('\n')
    owner_id = recipe.owner.id

    reviews_dict = []
    for review in reviews:
        user_profile = review.user_profile
        user = user_profile.user
        review_content = {
            'posterID': user.id,
            'posterName': user.username,
            'reviewContent': review.content
        }
        reviews_dict.append(review_content)

    context_dict['data'] = {
        'recipeId': recipe.id,
        'recipeTitle': recipe.title,
        'recipeOwner': owner_id,
        'recipeLike': recipe.likes,
        'recipeUrl': recipe.url,
        'recipeIngredients': ingredients,
        'recipeDirections': directions,
        'reviews': reviews_dict[::-1],
    }

    return JsonResponse(context_dict)


@login_required
def add_recipe(request):
    context_dict = {
        'success': True,
        'data': {

        }
    }
    category_name_slug = json.loads(request.body).get('slug')
    user = User.objects.get(id=json.loads(request.body).get('id'))
    try:
        category = Category.objects.get(slug=category_name_slug)
        user_profile = UserProfile.objects.get(user=user)
    except Category.DoesNotExist:
        category = None
        user_profile = None

    if category is None:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    recipe = Recipe.objects.create(category=category,
                                   owner=user_profile,
                                   title=json.loads(request.body).get('title'),
                                   ingredients=json.loads(request.body).get('ingredients'),
                                   directions=json.loads(request.body).get('directions'),
                                   url=json.loads(request.body).get('url'))

    context_dict['data']['status'] = 'ok'
    return JsonResponse(context_dict)


@login_required
def add_review(request, recipe_id):
    context_dict = {
        'success': True,
        'data': {},
    }
    recipe = Recipe.objects.get(id=recipe_id)
    user = User.objects.get(id=json.loads(request.body).get('id'))
    user_profile = UserProfile.objects.get(user=user)

    review = Review.objects.create(user_profile=user_profile, recipe=recipe,
                                   content=json.loads(request.body).get('content'))
    context_dict['success'] = True
    context_dict['data'] = {
        'userID': user.id,
        'userName': user.username,
    }

    return JsonResponse(context_dict)


@login_required
def recipe_add_like(request, recipe_id):
    context_dict = {
        'success': True,
        'data': {}
    }
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        recipe = None

    if recipe is None:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    likes = recipe.likes + 1
    recipe.likes = likes
    recipe.save()

    context_dict['data'] = {'likes': recipe.likes}

    return JsonResponse(context_dict)


@login_required
def show_my_recipe(request, user_id):
    context_dict = {
        'success': True,
        'data': {}
    }
    try:
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)
    except User.DoesNotExist:
        user = None
        user_profile = None

    if user is None:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    recipes = Recipe.objects.filter(owner=user_profile)
    recipe_list = []
    for recipe in recipes:
        recipe = {
            'recipeId': recipe.id,
            'recipeSlug': recipe.slug,
            'recipeTitle': recipe.title,
            'recipePic': recipe.url,
        }
        recipe_list.append(recipe)

    context_dict['data'] = {'recipes': recipe_list}

    return JsonResponse(context_dict)


@login_required
def show_favourite_recipe(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    favourite_recipe = FavouriteRecipe.objects.get_or_create(user=user_profile)[0]
    recipes = Recipe.objects.filter(favouriteRecipe=favourite_recipe)

    context_dict = add_recipes_to_dict(recipes)

    return JsonResponse(context_dict)


@login_required
def add_to_favourite_recipe(request):
    context_dict = {
        'success': True,
        'data': {}
    }

    user = User.objects.get(id=json.loads(request.body).get('userId'))
    recipe = Recipe.objects.get(id=json.loads(request.body).get('recipeId'))
    user_profile = UserProfile.objects.get(user=user)
    favourite_recipe = FavouriteRecipe.objects.get_or_create(user=user_profile)[0]
    recipe.favouriteRecipe.add(favourite_recipe)

    context_dict['data'] = {'status': 'ok'}

    return JsonResponse(context_dict)


@login_required
def search(request):
    keyword = json.loads(request.body).get('keyword')
    recipes = Recipe.objects.all()
    search_result = []
    for recipe in recipes:
        if keyword in recipe.title or keyword in recipe.ingredients:
            recipe_dict = {
                'recipeId': recipe.id,
                'recipeSlug': recipe.slug,
                'recipeTitle': recipe.title,
            }

            search_result.append(recipe_dict)

    context_dict = {
        'success': True,
        'data': {
            'keyword': keyword,
            'recipes': search_result,
        }
    }

    return JsonResponse(context_dict)


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


def register(request):
    context_dict = {
        'success': True,
        'data': {}
    }
    username = json.loads(request.body).get('username')
    password = json.loads(request.body).get('password')
    first_name = json.loads(request.body).get('firstName')
    last_name = json.loads(request.body).get('lastName')
    email = json.loads(request.body).get('email')
    user_tuple = User.objects.get_or_create(username=username)
    if not user_tuple[1]:
        # user already exist
        context_dict['data'] = {
            'status': 'error',
        }
        return JsonResponse(context_dict)

    u1 = user_tuple[0]
    u1.password = make_password(password, None, 'pbkdf2_sha256')
    u1.is_superuser = False
    u1.first_name = first_name
    u1.last_name = last_name
    u1.email = email
    u1.save()
    up = UserProfile.objects.create(user=u1)
    up.save()
    context_dict = {
        'success': True,
        'data': {
            'status': 'ok',
        }}
    return JsonResponse(context_dict)


def login(request):
    context_dict = {
        'success': True,
        'data': {}
    }

    username = json.loads(request.body).get('username')
    password = json.loads(request.body).get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        context_dict['data'] = {
            'status': 'error',
            'access': 'guest'
        }
        return JsonResponse(context_dict)

    auth.login(request, user)
    if user.is_superuser:
        context_dict['data'] = {
            'status': 'ok',
            'access': 'admin'
        }
    else:
        context_dict['data'] = {
            'status': 'ok',
            'access': 'user'
        }

    return JsonResponse(context_dict)


def get_user_info(request):
    context_dict = {
        'success': True,
        'data': {}
    }
    user = request.user

    if not user.is_authenticated:
        context_dict['data'] = {
            'access': 'guest',
            'status': 'error'
        }
        return JsonResponse(context_dict)

    if user.is_superuser:
        context_dict = {
            'success': True,
            'data': {
                'userName': user.username,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'id': user.id,
                'email': user.email,
                'access': 'admin',
                'status': 'ok'
            }
        }
    else:
        context_dict = {
            'success': True,
            'data': {
                'userName': user.username,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'id': user.id,
                'email': user.email,
                'access': 'user',
                'status': 'ok'
            }
        }

    return JsonResponse(context_dict)


@login_required
def logout(request):
    auth.logout(request)
    context_dict = {
        'success': True,
        'data': {}
    }
    return JsonResponse(context_dict)


@login_required
def update_password(request):
    context_dict = {
        'success': True,
        'data': {}
    }

    username = request.user.username
    try:
        u1 = User.objects.get(username=username)
    except User.DoesNoneExist:
        u1 = None

    if u1 is None:
        context_dict['data'] = {'status': 'error'}
        return JsonResponse(context_dict)

    old_plain_password = json.loads(request.body).get('oldPassword')
    # depend if user know his/her old password
    same = check_password(old_plain_password, u1.password)
    if not same:
        context_dict['data'] = {'status': 'error'}
        return JsonResponse(context_dict)

    new_plain_password = json.loads(request.body).get('newPassword')

    if new_plain_password == old_plain_password:
        # change the password to the same password
        context_dict = {
            'success': True,
            'data': {
                'status': 'error',
            }
        }
        return JsonResponse(context_dict)
    else:
        new_password = make_password(new_plain_password, None, 'pbkdf2_sha256')
        u1.password = new_password
        u1.save()
        context_dict = {
            'success': True,
            'data': {
                'status': 'ok',
            }
        }
        return JsonResponse(context_dict)


def bing_search(request):
    bing_key = "f9332617e5b046dba910de810c7a0829"
    search_url = 'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': request.GET.get('q'), 'textDecorations': True, 'textFormat': 'HTML'}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title': result['name'],
            'link': result['url'],
            'summary': result['snippet']})
    context_dict = {
        'success': True,
        'data': {
            'results': results,
        }
    }
    return JsonResponse(context_dict)


def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'token': token})
