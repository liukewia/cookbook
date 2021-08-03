from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rango.forms import CategoryForm, PageForm
from rango.models import Category, Page, Recipe, FavouriteRecipe


def index(request):
    return render(request, 'index.html')


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


# def get_all_recipes(request):
#     category_list = Category.objects.order_by('id')
#     categories = []
#     for category in category_list:
#         category_dict = {
#             'categoryName': category.name,
#             'categorySlug': category.slug,
#         }
#         categories.append(category_dict)
#
#     context_dict = {
#         'success': True,
#         'data': {
#             'categories': categories
#         }
#     }
#
#     return JsonResponse(context_dict)


def user_operation_demo(request):
    return JsonResponse({
        'success': True,
        'data': {
            'name': 'mockusername',
            'avatar': 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
            'firstName': 'mock',
            'lastName': 'user',
            'userid': 1,
            'email': 'antdesign@alipay.com',
            'access': 'user',
            # 'guest' means not logged in, 'user' means logged in, 'admin' means logged in and is super user.
        },
    })


# def user_login(request):
#     return render(request, 'user/login/index.html')


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
            'recipe_id': recipe.id,
            'recipe_title': recipe.title,
            'recipe_like': recipe.likes,
            'recipe_url': recipe.url,
        }
        recipes_dict.append(recipe_dict)

    context_dict = {
        'success': True,
        'data': {
            'category_id': category.id,
            'category_name': category.name,
            'category_likes': category.likes,
            'category_slug': category.slug,
            'recipes': recipes_dict,
        }
    }

    return JsonResponse(context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # redirected to home page
            return redirect('')
        else:
            print(form.errors)

    context_dict = {
        'success': True,
        'data': {
            'form': form,
        }
    }

    return JsonResponse(context_dict)


def show_recipe(request, recipe_title):
    context_dict = {}

    recipe = Recipe.objects.get(title=recipe_title)
    context_dict['recipe'] = recipe

    return render(request, '', context=context_dict)


@login_required
def show_favourite_recipe(request):
    context_dict = {}

    favourite_recipe = FavouriteRecipe.objects.get(id=request.GET.get('id'))
    recipes = Recipe.objects.filter(favouriteRecipe=favourite_recipe)
    context_dict['recipes'] = recipes

    return render(request, '', context=context_dict)


@login_required
def add_to_favourite_recipe(request):
    username = request.user.get_username
    recipe_id = request.GET.get('id')

    user = User.objects.filter(username=username).first()
    recipe = Recipe.objects.filter(id=recipe_id)
    favourite_recipe = FavouriteRecipe.objects.filter(user=user)
    recipe.favouriteRecipe.add(favourite_recipe)

    return render(request, '', context=None)


# def index(request):
#     category_list = Category.objects.order_by('-likes')[:5]
#     page_list = Page.objects.order_by('-views')[:5]
#
#     context_dict = {}
#     context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
#     context_dict['categories'] = category_list
#     context_dict['pages'] = page_list
#
#     visitor_cookie_handler(request)
#
#     response = render(request, 'rango/index.html', context=context_dict)
#     return response


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'about/index.html', context=context_dict)


# def show_category(request, category_name_slug):
#     context_dict = {}
#
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#         pages = Page.objects.filter(category=category)
#         context_dict['pages'] = pages
#         context_dict['category'] = category
#     except Category.DoesNotExist:
#         context_dict['category'] = None
#         context_dict['pages'] = None
#
#     return render(request, 'rango/category.html', context=context_dict)


# @login_required
# def add_category(request):
#     form = CategoryForm()
#
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('/rango/')
#         else:
#             print(form.errors)
#
#     return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug':
                                                    category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


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
