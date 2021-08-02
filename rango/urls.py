from django.urls import path, re_path

from rango import views

app_name = 'rango'

urlpatterns = [
    # match the root
    path('', views.index),
    # match all other pages
    # https://stackoverflow.com/questions/40826295/react-routing-and-django-url-conflict
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    re_path(r'^(?:.*)/?$', views.index),
    # path('user/login/', views.user_login),

    # path('about/', views.about, name="about"),
    # path('add_category/', views.add_category, name='add_category'),
    # path('category/<slug:category_name_slug>/add_page/',
    #      views.add_page, name='add_page'),
    # path('restricted/', views.restricted, name='restricted'),
]
