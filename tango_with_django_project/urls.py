"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from rango import views

urlpatterns = [
                  # match the root
                  path('', views.index),

                  # 后端接口放root和re_path中间
                  path('api/', include('rango.urls')),

                  # match all other pages
                  # https://stackoverflow.com/questions/40826295/react-routing-and-django-url-conflict
                  re_path(r'^(?:.*)/?$', views.index),

                  # path('user/login/', views.user_login),
                  # path('', views.index, name='index'),
                  # path('rango/', include('rango.urls')),
                  # path('admin/', admin.site.urls),
                  # path('accounts/', include('registration.backends.simple.urls')),
              ] + static(settings.STATIC_URL)
