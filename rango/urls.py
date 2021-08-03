from django.urls import path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('currentUser', views.user_operation_demo),
    path('add_category/', views.add_category, name='add_category'),

    # path('about/', views.about, name="about"),
    # path('user/login/', views.user_login),
    # path('category/<slug:category_name_slug>/add_page/',
    #      views.add_page, name='add_page'),
    # path('restricted/', views.restricted, name='restricted'),
]
