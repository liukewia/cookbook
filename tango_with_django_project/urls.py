from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from rango import views

urlpatterns = [
                  # match the root
                  path('', views.index),
                  path('api/', include('rango.urls')),

                  # match all other pages
                  re_path(r'^(?:.*)/?$', views.index),
              ] + static(settings.STATIC_URL)
