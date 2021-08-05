from django.urls import path, re_path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('currentUser/', views.user_operation_demo),
    path('add_category/', views.add_category),
    path('show_favourite_recipe/', views.show_favourite_recipe, name='show_favourite_recipe'),
    path('add_to_favourite_recipe/', views.add_to_favourite_recipe, name='add_to_favourite_recipe'),
    path('get_all_categories/', views.get_all_categories),
    path('get_all_recipes/', views.get_all_recipes),
    path('recipe/<int:recipe_id>/', views.show_recipe),
    path('add_recipe/', views.add_recipe),
    path('recipe/<int:recipe_id>/add_review/', views.add_review),
    path('<int:user_id>/my_recipe/', views.show_my_recipe),
    path('category/<slug:category_name_slug>/cate_add_like/', views.category_add_like),
    path('recipe/<int:recipe_id>/rec_add_like/', views.recipe_add_like),
    path('search/', views.search),
    path('user/login/', views.login),
    path('user/register/', views.register),
    path('user/getuserinfo/', views.getuserinfo),
    #path('user/changeuserinfo/', views.changeuserinfo),
    path('user/updatePassword/', views.updatePassword),
    path('user/updateInfo/', views.updateInfo),
    path('user/logout/', views.logout),

    re_path(r'^(?:.*)/?$', views.illegal_request_handler),
]
