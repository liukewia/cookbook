from django.urls import path, re_path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('category/<slug:category_name_slug>/', views.show_category),
    path('add_category/', views.add_category),
    path('show_favourite_recipe/<int:user_id>/', views.show_favourite_recipe),
    path('add_to_favourite_recipe/', views.add_to_favourite_recipe),
    path('get_all_categories/', views.get_all_categories),
    path('get_all_recipes/', views.get_all_recipes),
    path('recipe/<int:recipe_id>/', views.show_recipe),
    path('add_recipe/', views.add_recipe),
    path('recipe/<int:recipe_id>/add_review/', views.add_review),
    path('my_recipe/<int:user_id>/', views.show_my_recipe),
    path('category/<slug:category_name_slug>/cate_add_like/', views.category_add_like),
    path('recipe/<int:recipe_id>/rec_add_like/', views.recipe_add_like),
    path('bing_search', views.bing_search),
    path('user/login/', views.login),
    path('user/register/', views.register),
    path('user/getuserinfo/', views.get_user_info),
    path('user/update_password/', views.update_password),
    path('user/logout/', views.logout),

    re_path(r'^(?:.*)/?$', views.illegal_request_handler),
]
