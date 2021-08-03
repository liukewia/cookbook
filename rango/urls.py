from django.urls import path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('currentUser/', views.user_operation_demo),
    path('add_category/', views.add_category, name='add_category'),
    path('show_favourite_recipe/', views.show_favourite_recipe, name='show_favourite_recipe'),
    path('add_to_favourite_recipe/', views.add_to_favourite_recipe, name='add_to_favourite_recipe'),
    path('get_all_categories', views.get_all_categories)

    # path('about/', views.about, name="about"),
    # path('user/login/', views.user_login),
    # path('category/<slug:category_name_slug>/add_page/',
    #      views.add_page, name='add_page'),
    # path('restricted/', views.restricted, name='restricted'),
]
