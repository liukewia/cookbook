from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rango.forms import CategoryForm, RecipeForm
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
    recipe_list = Recipe.objects.order_by('-likes')
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
    cat_tuple = Category.objects.get_or_create(name=request.POST.get('name'))
    context_dict = {
        'success': True,
    }
    if not cat_tuple[1]:
        context_dict['error'] = "the category is already existed"

    return JsonResponse(context_dict)


def show_recipe(request, recipe_title_slug):
    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        reviews = Review.objects.filter(recipe=recipe)
    except Recipe.DoesNotExist:
        recipe = None
        reviews = None

    ingredients = recipe.ingredients.split('\n')
    directions = recipe.directions.split('\n')

    reviews_dict = []
    for review in reviews:
        review_content = {'reviewContent': review.content}
        reviews_dict.append(review_content)

    context_dict = {
        'success': True,
        'data': {
            'recipe_id': recipe.id,
            'recipe_title': recipe.title,
            'recipe_like': recipe.likes,
            'recipe_url': recipe.url,
            'recipe_ingredients': ingredients,
            'recipe_directions': directions,
            'reviews': reviews_dict,
        }
    }

    return JsonResponse(context_dict)


@login_required
def add_recipe(request):
    context_dict = {
        'success': True,
    }
    category_name_slug = request.POST.get('slug')
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        context_dict['success'] = False
        return JsonResponse(context_dict)

    recipe = Recipe.objects.create(category=category,
                                   title=request.POST.get('title'),
                                   ingredients=request.POST.get('ingredients'),
                                   directions=request.POST.get('directions'),
                                   url=request.POST.get('url'))

    return JsonResponse(context_dict)


@login_required
def add_review(request, recipe_title_slug):
    recipe = Recipe.objects.get(slug=recipe_title_slug)
    user = User.objects.get(id=request.POST.get('id'))
    user_profile = UserProfile.objects.get(user=user)

    review = Review.objects.create(user_profile=user_profile, recipe=recipe, content=request.POST.get('content'))
    context_dict = {'success': True, }

    return JsonResponse(context_dict)



@login_required
def show_favourite_recipe(request):

    favourite_recipe = FavouriteRecipe.objects.get(id=request.GET.get('id'))
    recipes = Recipe.objects.filter(favouriteRecipe=favourite_recipe)

    recipes_dict = []
    for recipe in recipes:
        recipe = {
            'recipe_id': recipe.id,
            'recipe_slug': recipe.slug,
            'recipe_title': recipe.title,
        }
        recipes_dict.append(recipe)

    context_dict = {
        'success': True,
        'data': {
            'recipes': recipes_dict,
        }
    }

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


# @login_required
# def add_page(request, category_name_slug):
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#     except Category.DoesNotExist:
#         category = None
#
#     if category is None:
#         return redirect('/rango/')
#
#     form = PageForm()
#
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#
#         if form.is_valid():
#             if category:
#                 page = form.save(commit=False)
#                 page.category = category
#                 page.views = 0
#                 page.save()
#
#                 return redirect(reverse('rango:show_category',
#                                         kwargs={'category_name_slug':
#                                                     category_name_slug}))
#         else:
#             print(form.errors)
#
#     context_dict = {'form': form, 'category': category}
#     return render(request, 'rango/add_page.html', context=context_dict)


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


'''auth_user: 先写下简单的逻辑
id int
password string
last_login datetime
is_superuser bool
username string
first_name string
email string
is_staff bool
is_active
date_joined
last_name



# 注册页面
def register():
    if request.method == 'GET':
        getusername = session.get('username')  # 从前端得到用户名
        getpassword = session.get('password')  # 从前端得到密码
        getfirst_name = session.get('first_name')  # 从前端得到用户名
        getlast_name = session.get('last_name')  # 从前端得到用户名
        getemail = session.get('email')  # 从前端得到邮箱
        # getuser_id = session.get('id')  # 从前端得到用户id
        # 获得当前时间curr_time_str
        curr_time = datetime.now()
        date_joined = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        # 将cdate_joined这个当前时间存入数据库
        db.session.commit()  # 存入数据库

    if request.method == 'POST':
        return redirect('/login')


# 登录页面
def login():
    if request.method == 'GET':
        # 用户输入
        enterusername = request.form.get('username')
        enterpassword = request.form.get('password')
        u1 = username.query.filter_by(username=enterusername).first()
        if enterpassword == u1.password:
            print("密码正确")
            # 改变用户状态登录中
            getusername = session.get('username')  # 前端得到顾客的username
            u_1 = user.query.filter_by(username=getusername).first()  # 得到id
            u_1.is_active = 'online'
            db.session.commit()  # 存入数据库
            return render_template('user.html')  # 进入用户页面
        else:
            print("密码错误")
            return render_template('login.html')  # 返回登录页面
    if request.method == 'POST':
        return redirect('/login')


# 登出页面
def logout():
    if request.method == 'GET':
    if request.method == 'POST':
            # 改变用户状态离线
            getusername = session.get('username')  # 前端得到顾客的username
            u_1 = user.query.filter_by(username=getusername).first()  # 通过username查询数据库得到id
            u_1.is_active = 'offline'
            db.session.commit()  # 存入数据库
            return redirect('/login')

# 个人密码更新
def changeinfo():
    if request.method == 'POST':
        getusername = session.get('username')  # 从前端得到用户名
        u1 = user.query.filter_by(username=getusername).first()  # 从数据库查到用户
        newpassword = session.get('password')  # 从前端得到新密码
        u1.password = newpassword  # 存入新密码
        db.session.commit()  # 保持数据库

'''
