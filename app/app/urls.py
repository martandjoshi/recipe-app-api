from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
]
